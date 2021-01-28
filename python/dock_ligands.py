import os
import re

import pandas as pd
from tqdm import tqdm

RECEPTOR = "../data/chimera/autodock.receptor.pdbqt"
LIGANDS = pd.read_csv(
    '../data/zinc/LRFVTYWOQMYALW-UHFFFAOYSA-N-biogenic.csv')['zinc_id'].tolist()

energies = dict()

for ligand in tqdm(LIGANDS):
    output = os.popen(
        f'vina --receptor="{RECEPTOR}" --ligand="../data/zinc/{ligand}.pdbqt" --center_x="-8.74645" --center_y="67.9434" --center_z="54.9447" --size_x="60.0059" --size_y="95.7474" --size_z="44.6495"').read()
    try:
        energy = float(re.findall(r'   1\s+(-?[0-9]+\.[0-9]+)', output)[0])
        energies[ligand] = energy
    except IndexError:
        pass

print(
    f'Minimum energy ligand: {min(energies.items(), key=lambda x: x[1])}')
