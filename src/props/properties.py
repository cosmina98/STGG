# Adapted from https://github.com/wengong-jin/hgraph2graph/

import rdkit
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
import rdkit.Chem.QED as QED
import networkx as nx
import props.sascorer as sascorer

from rdkit.rdBase import BlockLogs

def similarity(a, b):
    amol = Chem.MolFromSmiles(a)
    bmol = Chem.MolFromSmiles(b)
    fp1 = AllChem.GetMorganFingerprintAsBitVect(amol, 2, nBits=2048, useChirality=False)
    fp2 = AllChem.GetMorganFingerprintAsBitVect(bmol, 2, nBits=2048, useChirality=False)
    return DataStructs.TanimotoSimilarity(fp1, fp2)

def penalized_logp(s):
    mol = Chem.MolFromSmiles(s)

    logP_mean = 2.4570953396190123
    logP_std = 1.434324401111988
    SA_mean = -3.0525811293166134
    SA_std = 0.8335207024513095
    cycle_mean = -0.0485696876403053
    cycle_std = 0.2860212110245455

    log_p = Descriptors.MolLogP(mol)
    SA = -sascorer.calculateScore(mol)

    # cycle score
    cycle_list = nx.cycle_basis(nx.Graph(Chem.rdmolops.GetAdjacencyMatrix(mol)))
    if len(cycle_list) == 0:
        cycle_length = 0
    else:
        cycle_length = max([len(j) for j in cycle_list])
    if cycle_length <= 6:
        cycle_length = 0
    else:
        cycle_length = cycle_length - 6
    cycle_score = -cycle_length

    normalized_log_p = (log_p - logP_mean) / logP_std
    normalized_SA = (SA - SA_mean) / SA_std
    normalized_cycle = (cycle_score - cycle_mean) / cycle_std
    return normalized_log_p + normalized_SA + normalized_cycle


if __name__ == "__main__":
    print(
        round(
            penalized_logp("ClC1=CC=C2C(C=C(C(C)=O)C(C(NC3=CC(NC(NC4=CC(C5=C(C)C=CC=C5)=CC=C4)=O)=CC=C3)=O)=C2)=C1"), 2
        ),
        5.30,
    )
