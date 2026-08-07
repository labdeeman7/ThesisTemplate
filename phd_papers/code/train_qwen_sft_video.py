#!/usr/bin/env python3
"""Train Qwen3-VL SFT directly from JSONL examples, without tensor caching."""

from __future__ import annotations

import argparse
import json
import os
import random
from pathlib import Path
from typing import Any

import numpy as np
import torch
from datasets import Sequence, Value, load_dataset
from PIL import Image
from peft import LoraConfig, get_peft_model
from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
    BitsAndBytesConfig,
    EarlyStoppingCallback,
    Trainer,
    TrainerCallback,
    TrainingArguments,
)
from transformers.trainer_utils import get_last_checkpoint


torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True


def set_seed(seed: int = 42):
    """Make training as deterministic as the CUDA stack reasonably allows."""

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


class EpochLoggerCallback(TrainerCallback):
    """Print clear epoch boundaries to stdout."""

    def on_epoch_begin(self, args, state, control, **kwargs):
        print(f">>> Starting Epoch {int(state.epoch or 0) + 1}/{args.num_train_epochs}")

    def on_epoch_end(self, args, state, control, **kwargs):
        print(f">>> Finished Epoch {int(state.epoch or 0)}/{args.num_train_epochs}\n")


class MemoryStatsCallback(TrainerCallback):
    """Log GPU memory at normal Trainer logging events."""

    def on_log(self, args, state, control, logs=None, **kwargs):
        if torch.cuda.is_available():
            mem_alloc = torch.cuda.memory_allocated(0) / 1e9
            mem_reserved = torch.cuda.memory_reserved(0) / 1e9
            print(f"[MEM] Alloc: {mem_alloc:.2f} GB | Reserved: {mem_reserved:.2f} GB")


def parse_args():
    """Collect JSONL, model, vision-size, and LoRA/training arguments."""

    p = argparse.ArgumentParser()
    p.add_argument("--model_name", type=str, default="Qwen/Qwen3-VL-8B-Instruct")
    p.add_argument(
        "--dataset_root",
        type=str,
        required=True,
        help="Dataset root containing train/val/test split folders.",
    )
    p.add_argument(
        "--experiment_name",
        type=str,
        default=None,
        help="JSONL suffix, e.g. video_5frame_stride1 for sft_train_video_5frame_stride1.jsonl.",
    )
    p.add_argument("--train_jsonl", type=str, default=None, help="Explicit train JSONL path.")
    p.add_argument("--val_jsonl", type=str, default=None, help="Explicit validation JSONL path.")
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--deepspeed", type=str, default=None)

    # Vision token budget. Cache training used 384x384; 5-frame no-cache defaults
    # lower so each sample has a smaller visual graph.
    p.add_argument("--image_max_pixels", type=int, default=256 * 256)
    p.add_argument("--image_min_pixels", type=int, default=64 * 64)

    # Batching
    p.add_argument("--train_bs", type=int, default=1)
    p.add_argument("--eval_bs", type=int, default=1)
    p.add_argument("--grad_accum", type=int, default=32)

    # Training
    p.add_argument("--num_train_epochs", type=int, default=5)
    p.add_argument("--lr", type=float, default=2e-4)
    p.add_argument("--warmup_ratio", type=float, default=0.03)
    p.add_argument("--weight_decay", type=float, default=0.01)
    p.add_argument("--max_grad_norm", type=float, default=1.0)

    # LoRA
    p.add_argument("--lora_r", type=int, default=64)
    p.add_argument("--lora_alpha", type=int, default=128)
    p.add_argument("--lora_dropout", type=float, default=0.05)
    p.add_argument("--freeze_visual", action=argparse.BooleanOptionalAction, default=True)

    # Misc
    p.add_argument("--seed", type=int, default=42)
    p.add_argument(
        "--optim",
        type=str,
        default="adamw_torch_fused",
        choices=["adamw_torch", "adamw_torch_fused", "adamw_bnb_8bit"],
    )
    p.add_argument(
        "--attn_implementation",
        type=str,
        default="flash_attention_2",
        choices=["flash_attention_2", "sdpa", "eager"],
    )
    p.add_argument(
        "--eval_frequency_ratio",
        type=float,
        default=1.0,
        help="Eval every X fraction of total steps. 1.0 means every epoch; 0.05 means every 5 percent.",
    )
    p.add_argument("--early_stopping_patience", type=int, default=5)
    p.add_argument("--early_stopping_threshold", type=float, default=0.0)
    p.add_argument("--save_total_limit", type=int, default=10)
    p.add_argument("--num_workers", type=int, default=4)
    p.add_argument("--resume", action=argparse.BooleanOptionalAction, default=True)
    return p.parse_args()


def resolve_jsonl_paths(args) -> tuple[Path, Path]:
    """Resolve train/validation JSONLs from explicit paths or an experiment suffix."""

    dataset_root = Path(args.dataset_root)
    if args.train_jsonl or args.val_jsonl:
        if not (args.train_jsonl and args.val_jsonl):
            raise ValueError("Pass both --train_jsonl and --val_jsonl, or neither.")
        train_jsonl = Path(args.train_jsonl)
        val_jsonl = Path(args.val_jsonl)
    elif args.experiment_name:
        train_jsonl = dataset_root / "train" / f"sft_train_{args.experiment_name}.jsonl"
        val_jsonl = dataset_root / "val" / f"sft_val_{args.experiment_name}.jsonl"
    else:
        train_jsonl = dataset_root / "train" / "sft_train.jsonl"
        val_jsonl = dataset_root / "val" / "sft_val.jsonl"

    for jsonl_path in (train_jsonl, val_jsonl):
        if not jsonl_path.exists():
            raise FileNotFoundError(f"Missing dataset JSONL: {jsonl_path}")
    return train_jsonl, val_jsonl


def messages_to_qwen_text(processor, messages: list[dict[str, Any]], add_generation_prompt: bool) -> str:
    """Render chat messages exactly as Qwen expects before tokenization."""

    return processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=add_generation_prompt,
    )


def find_last_assistant_index(messages: list[dict[str, Any]]) -> int:
    """Return the index of the supervised assistant message."""

    for i in range(len(messages) - 1, -1, -1):
        if messages[i].get("role") == "assistant":
            return i
    raise ValueError("No assistant message found in SFT example.")


class QwenJSONLCollator:
    """Load images, tokenize chat text, and mask labels to assistant tokens only."""

    def __init__(self, processor):
        self.processor = processor

    def __call__(self, features):
        full_texts = []
        prefix_texts = []
        image_batches = []

        for ex in features:
            messages = ex["messages"]
            assistant_idx = find_last_assistant_index(messages)

            # Full text includes the target answer. Prefix text stops just before
            # the answer but includes Qwen's assistant-generation marker.
            full_texts.append(messages_to_qwen_text(self.processor, messages, add_generation_prompt=False))
            prefix_texts.append(
                messages_to_qwen_text(
                    self.processor,
                    messages[:assistant_idx],
                    add_generation_prompt=True,
                )
            )
            image_batches.append([Image.open(p).convert("RGB") for p in ex["images"]])

        batch = self.processor(
            text=full_texts,
            images=image_batches,
            padding=True,
            return_tensors="pt",
        )
        prefix_batch = self.processor(
            text=prefix_texts,
            images=image_batches,
            padding=True,
            return_tensors="pt",
        )

        labels = batch["input_ids"].clone()
        labels[labels == self.processor.tokenizer.pad_token_id] = -100

        # The prompt length includes image tokens, so we compute it with the
        # processor rather than with the tokenizer alone.
        for i in range(labels.shape[0]):
            prompt_len = prefix_batch["attention_mask"][i].sum().item()
            labels[i, :prompt_len] = -100

        batch["labels"] = labels
        return batch


def configure_processor(args):
    """Load the Qwen processor and apply the requested visual token budget."""

    processor = AutoProcessor.from_pretrained(
        args.model_name,
        trust_remote_code=True,
        use_fast=True,
    )
    processor.image_processor.max_pixels = args.image_max_pixels
    processor.image_processor.min_pixels = args.image_min_pixels
    return processor


def load_lora_model(args):
    """Load Qwen3-VL in 4-bit and attach trainable LoRA adapters."""

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
    )
    model = AutoModelForImageTextToText.from_pretrained(
        args.model_name,
        quantization_config=bnb_config,
        trust_remote_code=True,
        attn_implementation=args.attn_implementation,
    )

    if args.freeze_visual and hasattr(model, "model") and hasattr(model.model, "visual"):
        for p in model.model.visual.parameters():
            p.requires_grad = False
        print("Visual encoder frozen")

    target_modules = [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ]
    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=target_modules,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    return model


def compute_eval_steps(num_train_examples: int, args) -> int:
    """Match the cache trainer's eval cadence calculation."""

    steps_per_epoch = num_train_examples // (args.train_bs * args.grad_accum)
    steps_per_epoch = max(1, steps_per_epoch)
    total_steps = steps_per_epoch * args.num_train_epochs
    if args.eval_frequency_ratio < 1.0:
        return max(1, int(total_steps * args.eval_frequency_ratio))
    return steps_per_epoch


def main():
    """Train LoRA adapters from raw JSONL examples and image paths."""

    args = parse_args()
    set_seed(args.seed)
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

    train_jsonl, val_jsonl = resolve_jsonl_paths(args)
    data_files = {"train": str(train_jsonl), "validation": str(val_jsonl)}
    dataset = load_dataset("json", data_files=data_files)
    dataset = dataset.cast_column("images", Sequence(Value("string")))
    print(f"Train samples: {len(dataset['train'])} | Val samples: {len(dataset['validation'])}")
    print(f"Image pixel caps: min={args.image_min_pixels} max={args.image_max_pixels}")

    processor = configure_processor(args)
    model = load_lora_model(args)

    eval_steps = compute_eval_steps(len(dataset["train"]), args)
    common_args = dict(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.train_bs,
        per_device_eval_batch_size=args.eval_bs,
        gradient_accumulation_steps=args.grad_accum,
        num_train_epochs=args.num_train_epochs,
        learning_rate=args.lr,
        bf16=True,
        tf32=True,
        remove_unused_columns=False,
        report_to=["wandb"],
        eval_strategy="steps",
        save_strategy="steps",
        save_steps=eval_steps,
        eval_steps=eval_steps,
        save_total_limit=args.save_total_limit,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        logging_steps=max(1, eval_steps // 4),
        dataloader_num_workers=args.num_workers,
        dataloader_pin_memory=True,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        max_grad_norm=args.max_grad_norm,
        optim=args.optim,
        gradient_checkpointing=True,
    )
    if args.deepspeed:
        if torch.cuda.device_count() <= 1:
            raise RuntimeError("DeepSpeed requires multiple GPUs.")
        training_args = TrainingArguments(deepspeed=args.deepspeed, **common_args)
    else:
        training_args = TrainingArguments(**common_args)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"],
        data_collator=QwenJSONLCollator(processor),
        callbacks=[
            EpochLoggerCallback(),
            MemoryStatsCallback(),
            EarlyStoppingCallback(
                early_stopping_patience=args.early_stopping_patience,
                early_stopping_threshold=args.early_stopping_threshold,
            ),
        ],
    )

    last_checkpoint = None
    if args.resume and Path(args.output_dir).exists():
        last_checkpoint = get_last_checkpoint(args.output_dir)

    if last_checkpoint is not None:
        print(f"Resuming from checkpoint: {last_checkpoint}")
        trainer.train(resume_from_checkpoint=last_checkpoint)
    else:
        print("No checkpoint found, starting fresh.")
        trainer.train()

    final_dir = Path(args.output_dir) / "final_checkpoint"
    trainer.save_model(str(final_dir))
    print(f"Training complete. Final model saved to {final_dir}")


if __name__ == "__main__":
    main()
