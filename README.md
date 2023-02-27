# spanning_tree_based_molecule_generation

## 1. Setting up neptune
You need to get a (free) neptune account and modify the YOUR_API_KEY and YOUR_PROJECT_KEY for neptune initialization (in our files train_generator.py, train_smiles_generator.py, train_condgenerator.py):


## 2. Setting up the environment
You can set up the environment by following commands. You can install the Dockerfile. Otherwise, you can run the following commands while specifying cudatoolkit version and torch geometric versions accordinly to your local computing device.

```
conda create -n mol python=3.7
source ~/.bashrc
conda activate mol
conda install -y pytorch cudatoolkit=10.1 -c pytorch
conda install -y tqdm
conda install -y -c conda-forge neptune-client
conda install -y -c conda-forge rdkit

pip install pytorch-lightning
pip install neptune-client[pytorch-lightning]

pip install torch-scatter -f https://pytorch-geometric.com/whl/torch-1.8.1+cu111.html
pip install torch-sparse -f https://pytorch-geometric.com/whl/torch-1.8.1+cu111.html
pip install torch-cluster -f https://pytorch-geometric.com/whl/torch-1.8.1+cu111.html
pip install torch-spline-conv -f https://pytorch-geometric.com/whl/torch-1.8.1+cu111.html
pip install torch-geometric

pip install cython
pip install molsets

```

## 3. Executing the scripts
For Table 2.

```
cd molgen/src/
CUDA_VISIBLE_DEVICES=${CPU} bash ../script/generator_zinc.sh
CUDA_VISIBLE_DEVICES=${CPU} bash ../script/generator_qm9.sh
```

For Table 3.

```
cd molgen/src/
CUDA_VISIBLE_DEVICES=${CPU} bash ../script/generator_zinc_A.sh
CUDA_VISIBLE_DEVICES=${CPU} bash ../script/generator_zinc_S.sh
CUDA_VISIBLE_DEVICES=${CPU} bash ../script/generator_zinc_ST.sh
CUDA_VISIBLE_DEVICES=${CPU} bash ../script/generator_zinc_STG.sh.sh
CUDA_VISIBLE_DEVICES=${CPU} bash ../script/generator_zinc_STGV.sh
```

For Table 4 and 5.

```
cd molgen/src/
CUDA_VISIBLE_DEVICES=${CPU} bash ../script/generator_moses.sh
```

For Table 6.

```
cd molgen/src/
CUDA_VISIBLE_DEVICES=${CPU} bash ../script/condgenerator_zinc.sh 
```