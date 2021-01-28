from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='../data/5k2c.pdb', model_segment=('FIRST:A', 'LAST:A'))
aln.append_model(mdl, align_codes='5k2cA', atom_files='../data/5k2c.pdb')
aln.append(file='../data/P29274.ali', align_codes='P29274')
aln.align2d()
aln.write(file='../data/P29274-5k2cA.ali', alignment_format='PIR')
aln.write(file='../data/P29274-5k2cA.pap', alignment_format='PAP')
