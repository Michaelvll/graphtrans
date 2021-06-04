#!/bin/bash
set -xe
conda create -n graph-aug python=3.8 -y
source activate graph-aug
conda install -n graph-aug pytorch=1.7 torchvision torchaudio cpuonly -c pytorch -y

TORCH=1.7.0
CUDA=cpu
pip install torch-scatter -f https://pytorch-geometric.com/whl/torch-${TORCH}+${CUDA}.html
pip install torch-sparse -f https://pytorch-geometric.com/whl/torch-${TORCH}+${CUDA}.html
pip install torch-cluster -f https://pytorch-geometric.com/whl/torch-${TORCH}+${CUDA}.html
pip install torch-spline-conv -f https://pytorch-geometric.com/whl/torch-${TORCH}+${CUDA}.html
pip install torch-geometric ogb configargparse wandb loguru tqdm numpy