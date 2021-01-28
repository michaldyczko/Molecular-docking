from urllib.request import urlretrieve

import pandas as pd
from modeller import *
from tqdm import tqdm

profile = pd.read_csv('../data/build_profile.prf',
                      sep='\s+', skiprows=7, index_col=1, header=None)

env = environ()
aln = alignment(env)
for (pdb, chain) in tqdm([(code[:-1], code[-1]) for code, identity, e_value in zip(profile.index, profile[10], profile[11]) if e_value == 0 and identity > 75]):
    try:
        with open(f'../data/{pdb}.pdb', 'r') as f:
            if "MUTATION: YES" in f.read():
                continue
    except FileNotFoundError:
        urlretrieve(
            f'https://files.rcsb.org/view/{pdb}.pdb', f'../data/{pdb}.pdb')
        with open(f'../data/{pdb}.pdb', 'r') as f:
            if "MUTATION: YES" in f.read():
                continue
    m = model(env, file=f'../data/{pdb}.pdb',
              model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)
