from urllib.request import urlretrieve

import openbabel
import pandas as pd
from tqdm import tqdm

substances = pd.read_csv(
    '../data/zinc/LRFVTYWOQMYALW-UHFFFAOYSA-N-biogenic.csv', index_col=0)

for zinc_id, _ in tqdm(zip(substances.index, substances.smiles)):

    urlretrieve(
        f'http://zinc.docking.org/substances/{zinc_id}.mol2', f'../data/zinc/{zinc_id}.mol2')

    obConversion = openbabel.OBConversion()
    obConversion.SetInAndOutFormats("mol2", "pdbqt")

    mol = openbabel.OBMol()
    obConversion.ReadFile(mol, f'../data/zinc/{zinc_id}.mol2')
    obConversion.WriteFile(mol, f'../data/zinc/{zinc_id}.pdbqt')
