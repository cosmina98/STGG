#!/bin/bash

python train_generator.py \
--dataset_name zinc \
--num_layers 3 \
--disable_valencemask \
--disable_graphmask \
--tag generator_zinc_ST