#!/usr/bin/env bash

: "${HF_TOKEN:?Set HF_TOKEN in the environment before running this script}"

export PYTHONUNBUFFERED=1

export WANDB_PROJECT=cholec-triplet-sft

cd /nfs/home/talabi/repositories/surg_prvit/

CUDA_VISIBLE_DEVICES=0 python train_sft_from_cache.py \
  --cache_dir ./datasets/processed_cholec_sft_direct/ \
  --output_dir ./output/processed_cholec_sft_direct \
  --train_bs 1 \
  --eval_bs 1 \
  --grad_accum 32 \
  --num_train_epochs 5 \
  --lr 2e-4 \
  --lora_r 64 \
  --lora_alpha 128 \
  --optim "adamw_torch_fused" \
  --seed 42 \
  --eval_frequency_ratio 0.05 
