from modeller import *
from modeller import soap_protein_od
from modeller.automodel import *

env = environ()
a = automodel(env, alnfile='../data/P29274-5k2cA_cut.ali',
              knowns='5k2cA', sequence='P29274',
              assess_methods=(assess.DOPE,
                              soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()
