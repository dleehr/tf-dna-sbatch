
# coding: utf-8

# In[34]:

import subprocess
import os
import itertools
import sys


# In[2]:

# Enumerate the model files, will be parsed

e2f_files = '''E2F1_250nM_Bound_filtered_normalized_34bp_GCGC_1a2a3mer_format.model
E2F1_250nM_Bound_filtered_normalized_34bp_GCGG_1a2a3mer_format.model
E2F4_500nM_Bound_filtered_normalized_34bp_GCGC_1a2a3mer_format.model
E2F4_500nM_Bound_filtered_normalized_34bp_GCGG_1a2a3mer_format.model'''

elkets_files = '''ELK1_100nM_Bound_filtered_normalized_GGAA_1a2a3mer_format.model
ELK1_100nM_Bound_filtered_normalized_GGAT_1a2a3mer_format.model
ETS1_100nM_Bound_filtered_normalized_GGAA_1a2a3mer_format.model
ETS1_100nM_Bound_filtered_normalized_GGAT_1a2a3mer_format.model'''

hismadmax_files ='''HisMadMax_Bound_filtered_normalized_CACATG_1a2a3mer_format.model
HisMadMax_Bound_filtered_normalized_CACGAG_1a2a3mer_format.model
HisMadMax_Bound_filtered_normalized_CACGCG_1a2a3mer_format.model
HisMadMax_Bound_filtered_normalized_CACGTG_1a2a3mer_format.model
HisMadMax_Bound_filtered_normalized_CATGCG_1a2a3mer_format.model
HisMycMax_Bound_filtered_normalized_CACATG_1a2a3mer_format.model
HisMycMax_Bound_filtered_normalized_CACGAG_1a2a3mer_format.model
HisMycMax_Bound_filtered_normalized_CACGCG_1a2a3mer_format.model
HisMycMax_Bound_filtered_normalized_CACGTG_1a2a3mer_format.model
HisMycMax_Bound_filtered_normalized_CATGCG_1a2a3mer_format.model
'''


# In[40]:

# Functions to parsae the modle file names

def parse_e2f(f):
    components = f.split('_')
    protein = components[0]
    width = components[5][:2]
    core = components[6]
    kmers = components[7].replace('mer','').split('a')
    return [protein, width, core, kmers]

def parse_elkets(f):
    components = f.split('_')
    protein = components[0]
    width = 36
    core = components[5]
    kmers = components[6].replace('mer','').split('a')
    return [protein, width, core, kmers]

def parse_hismadmax(f):
    components = f.split('_')
    protein = components[0]
    width = 36
    core = components[4]
    kmers = components[5].replace('mer','').split('a')
    return [protein, width, core, kmers]


# In[41]:

models = list()
for f in e2f_files.splitlines():
    models.append([f] + parse_e2f(f))
for f in elkets_files.splitlines():
    models.append([f] + parse_elkets(f))
for f in hismadmax_files.splitlines():
    models.append([f] + parse_hismadmax(f))


# In[42]:

genomes = ['hg19', 'hg38']
chroms = []
for x in range(1,23):
    chroms.append('chr{}'.format(x))
chroms.extend(['chrX','chrY'])


# In[57]:

combinations = [x for x in itertools.product(genomes, chroms, models)]

idx = int(sys.argv[1])
vals = combinations[idx]

assembly = vals[0]
chrom = vals[1]
params = vals[2]

model_filename = params[0]
protein = params[1]
width = params[2]
core = params[3]
kmers_list = params[4]

# predict_genome.py
#usage: predict_genome.py [-h] -g GenomeFile [--chroms [Chroms [Chroms ...]]]
#                         -m ModelFile -c Core -w Width -k Kmers [Kmers ...]
#                         [-i] -o OutputFile

# CONSTANTS
genome_files_dir = '/data/sciencesupport/tf-dna-predictions/genomes'
model_files_dir = '/data/sciencesupport/tf-dna-predictions/models/Ning/TF_general/SVR'
genome_file = '{}/{}.fa'.format(genome_files_dir, assembly)
model_file = '{}/{}'.format(model_files_dir, model_filename)
output_base = '/data/sciencesupport/tf-dna-predictions/results'
output_dir = '{}/{}/{}'.format(output_base, assembly, protein)
output_file = '{}/{}_{}_predictions.bed'.format(output_dir, model_filename, chrom)

# core set earlier
# width set earlier

# predict_genome
command = ['python', 'predict_genome.py', 
           '-g', genome_file, '--chroms', chrom, 
           '-m', model_file, '-c', core, 
           '-w', str(width), '-k']
command.extend(kmers_list)
command.extend(['-o', output_file])

try:
   os.makedirs(output_dir)
except OSError as e:
   pass # Tried to check if not exists first, but when we schedule multiple simultaneous jobs, it fails.
print ' '.join(command)

