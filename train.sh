# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
#!/bin/bash
set -e -x

CODE=src
DATA=musicnet/preprocessed

EXP=musicnet
export MASTER_PORT=29500

python src/train.py \
    --data musicnet/preprocessed/Bach_Solo_Cello  \
           musicnet/preprocessed/Bach_Solo_Piano \
    --batch-size 1 \
    --checkpoint checkpoints\pretrained_musicnet \
    --lr-decay 0.995 \
    --epoch-len 50 \
    --num-workers 3 \
    --lr 1e-3 \
    --seq-len 1200 \
    --d-lambda 1e-2 \
    --expName musicnet \
    --latent-d 128 \
    --layers 14 \
    --blocks 4 \
    --data-aug \
    --grad-clip 1