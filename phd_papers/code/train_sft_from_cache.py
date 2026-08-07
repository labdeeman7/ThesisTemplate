#!/usr/bin/env python3

import argparse
import json
import random
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset

from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
    TrainerCallback,
    EarlyStoppingCallback
)
from peft import LoraConfig, get_peft_model
from transformers.trainer_utils import get_last_checkpoint
# from utils.cache_utils import CachedVLSDataset, cached_collator
from functools import partial

# ----------------------------
# Reproducibility
# ----------------------------
def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

# Remember to use the utils later. For now, we keep the collator here for simplicity.
# ----------------------------
# Cached Dataset
# ----------------------------
class CachedVLSDataset(Dataset):
    def __init__(self, cache_dir: str, split: str):
        self.split_dir = Path(cache_dir) / split
        with open(self.split_dir / "index.json", "r") as f:
            self.files = json.load(f)
        self.column_names = ["input_ids", "labels", "pixel_values", "image_grid_thw"]

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        return torch.load(
            self.split_dir / self.files[idx],
            map_location="cpu",
            weights_only=True,
        )

# Remember to use the utils later. For now, we keep the collator here for simplicity.
# ----------------------------
# Cached Collator
# ----------------------------
def cached_collator(batch):
    return {
        "input_ids": torch.nn.utils.rnn.pad_sequence(
            [x["input_ids"] for x in batch], batch_first=True, padding_value=0
        ),
        "labels": torch.nn.utils.rnn.pad_sequence(
            [x["labels"] for x in batch], batch_first=True, padding_value=-100
        ),
        "attention_mask": torch.nn.utils.rnn.pad_sequence( 
            [x["attention_mask"] for x in batch], batch_first=True, padding_value=0 
        ),
        "pixel_values": torch.cat([x["pixel_values"] for x in batch], dim=0),
        "image_grid_thw": torch.cat([x["image_grid_thw"] for x in batch], dim=0),
    }

# ----------------------------
# Callbacks for Monitoring
# ----------------------------
class EpochLoggerCallback(TrainerCallback):
    """Prints clear epoch boundaries to stdout."""
    def on_epoch_begin(self, args, state, control, **kwargs):
        print(f">>> Starting Epoch {int(state.epoch)+1}/{args.num_train_epochs}")
    def on_epoch_end(self, args, state, control, **kwargs):
        print(f">>> Finished Epoch {int(state.epoch)}/{args.num_train_epochs}\n")

class MemoryStatsCallback(TrainerCallback):
    """Logs GPU memory stats every logging_step."""
    def on_log(self, args, state, control, logs=None, **kwargs):
        if torch.cuda.is_available():
            mem_alloc = torch.cuda.memory_allocated(0) / 1e9
            mem_reserved = torch.cuda.memory_reserved(0) / 1e9
            print(f"[MEM] Alloc: {mem_alloc:.2f} GB | Reserved: {mem_reserved:.2f} GB")

# ----------------------------
# Args
# ----------------------------
def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model_name", type=str, default="Qwen/Qwen3-VL-8B-Instruct")
    p.add_argument("--cache_dir", type=str, required=True)
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--deepspeed", type=str, default=None)
    
    # Batching
    p.add_argument("--train_bs", type=int, default=2)
    p.add_argument("--eval_bs", type=int, default=2)
    p.add_argument("--grad_accum", type=int, default=128)
    
    # Training
    p.add_argument("--num_train_epochs", type=int, default=10)
    p.add_argument("--lr", type=float, default=2e-5)
    p.add_argument("--warmup_ratio", type=float, default=0.03)
    p.add_argument("--weight_decay", type=float, default=0.01)
    p.add_argument("--max_grad_norm", type=float, default=1.0)
    
    # LoRA
    p.add_argument("--lora_r", type=int, default=64)
    p.add_argument("--lora_alpha", type=int, default=128)
    p.add_argument("--lora_dropout", type=float, default=0.05)
    
    # Misc
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--optim", type=str, default="adamw_torch_fused", 
                   choices=["adamw_torch", "adamw_torch_fused", "adamw_bnb_8bit"])
    p.add_argument("--max_seq_length", type=int, default=2048)
    p.add_argument("--eval_frequency_ratio", type=float, default=1.0,
               help="Eval every X% of total steps (1.0 = every epoch, 0.2 = 5× total)")
    p.add_argument("--early_stopping_patience", type=int, default=5)
    p.add_argument("--early_stopping_threshold", type=float, default=0.0)
    
    
    return p.parse_args()

# ----------------------------
# Main
# ----------------------------
def main():
    args = parse_args()
    set_seed(args.seed)

    # ---- Dataset ----
    train_ds = CachedVLSDataset(args.cache_dir, "train")
    val_ds   = CachedVLSDataset(args.cache_dir, "test")
    print(f"Train samples: {len(train_ds)} | Val samples: {len(val_ds)}")

    # ---- Model (QLoRA) ----
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
        attn_implementation="flash_attention_2",
    )
    
    # Freeze visual encoder (standard for VLM SFT)
    for p in model.model.visual.parameters():
        p.requires_grad = False

    # ---- LoRA ----
    target_modules = [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ]

    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,  # Fixed: 2x r
        lora_dropout=args.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=target_modules,
    )

    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    
    # ---- Dynamic Steps Calculation ----
    steps_per_epoch = len(train_ds) // (args.train_bs * args.grad_accum)
    steps_per_epoch = max(1, steps_per_epoch) 
    
    total_steps = steps_per_epoch * args.num_train_epochs
    
    if args.eval_frequency_ratio < 1.0:
        eval_steps = max(1, int(total_steps * args.eval_frequency_ratio))
    else:
        eval_steps = steps_per_epoch  # Default: every epoch

    
    # ---- Training Args ----
    common_args = dict(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.train_bs,
        per_device_eval_batch_size=args.eval_bs,  # Eval does NOT use grad_accum
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
        eval_steps=eval_steps,  # Fixed: Eval every epoch
        save_total_limit=10,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        logging_steps=max(1, steps_per_epoch // 4),  # Log 4x per epoch
        dataloader_num_workers=4,
        dataloader_pin_memory=True,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        max_grad_norm=args.max_grad_norm,
        optim=args.optim,
    )

    if args.deepspeed:
        assert torch.cuda.device_count() > 1, "DeepSpeed requires multi-GPU"
        print(f"Using DeepSpeed config: {args.deepspeed}")
        training_args = TrainingArguments(deepspeed=args.deepspeed, **common_args)
    else:
        training_args = TrainingArguments(**common_args)
    
    
    # ---- Trainer ----
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=cached_collator,
        callbacks=[EpochLoggerCallback(), 
                   MemoryStatsCallback(),
                   EarlyStoppingCallback(
                        early_stopping_patience=args.early_stopping_patience,
                        early_stopping_threshold=args.early_stopping_threshold,
                    ),
                ],  # Added callbacks
        )

    print(">>> Training from cache")
    last_checkpoint = None
    if Path(args.output_dir).exists():
        last_checkpoint = get_last_checkpoint(args.output_dir)

    if last_checkpoint is not None:
        print(f"Resuming from checkpoint: {last_checkpoint}")
        trainer.train(resume_from_checkpoint=last_checkpoint)
    else:
        print("No checkpoint found, starting fresh.")
        trainer.train()
    
    # Save final model explicitly
    trainer.save_model(args.output_dir + "/final_checkpoint")
    print(f"Training complete. Final model saved to {args.output_dir}/final_checkpoint")

if __name__ == "__main__":
    main()