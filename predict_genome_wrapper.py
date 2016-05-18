# coding: utf-8

import subprocess
import os
import itertools
import sys

# Enumerate the model files, will be parsed

e2f_files = '''E2F/E2F1_250nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGC_1a2a3mer_format.model
E2F/E2F1_250nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGG_1a2a3mer_format.model
E2F/E2F4_500nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGC_1a2a3mer_format.model
E2F/E2F4_500nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGG_1a2a3mer_format.model'''

elkets_files = '''ETS/ELK1_100nM_Bound_filtered_normalized_transformed_20bp_GGAA_1a2a3mer_format.model
ETS/ELK1_100nM_Bound_filtered_normalized_transformed_20bp_GGAT_1a2a3mer_format.model
ETS/ETS1_100nM_Bound_filtered_normalized_transformed_20bp_GGAA_1a2a3mer_format.model
ETS/ETS1_100nM_Bound_filtered_normalized_transformed_20bp_GGAT_1a2a3mer_format.model'''

hismadmax_files = '''bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CACATG_1a2a3mer_format.model
bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CACGAG_1a2a3mer_format.model
bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CACGCG_1a2a3mer_format.model
bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CACGTG_1a2a3mer_format.model
bHLH/HisMadMax_Bound_filtered_normalized_transformed_20bp_CATGCG_1a2a3mer_format.model
bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CACATG_1a2a3mer_format.model
bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CACGAG_1a2a3mer_format.model
bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CACGCG_1a2a3mer_format.model
bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CACGTG_1a2a3mer_format.model
bHLH/HisMycMax_Bound_filtered_normalized_transformed_20bp_CATGCG_1a2a3mer_format.model'''

# Functions to parsae the model file names
def parse_e2f(f):
    f = f.split('/')[1]
    components = f.split('_')
    protein = components[0]
    width = components[5][:2]
    core = components[6]
    kmers = components[7].replace('mer','').split('a')
    return [protein, width, core, kmers, False]

def parse_elkets(f):
    f = f.split('/')[1]
    components = f.split('_')
    protein = components[0]
    width = 36
    core = components[7]
    kmers = components[8].replace('mer','').split('a')
    return [protein, width, core, kmers, True]

def parse_hismadmax(f):
    f = f.split('/')[1]
    components = f.split('_')
    protein = components[0]
    width = 36
    core = components[4]
    kmers = components[5].replace('mer','').split('a')
    return [protein, width, core, kmers, True]


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

# CONSTANTS
genome_files_dir = '/data/sciencesupport/tf-dna-predictions/genomes'
model_files_dir = '/data/sciencesupport/tf-dna-predictions/models/Ning/TF_general/SVR/model_files_final'
output_base = '/data/sciencesupport/tf-dna-predictions/results'

def output_file_name(output_dir, model_filename, chrom):
    return '{}/{}_{}_predictions.bed'.format(output_dir, model_filename, chrom)

def output_dir_name(output_base, assembly, protein):
    return '{}/{}/{}'.format(output_base, assembly, protein)

if __name__ == '__main__':
    combinations = [x for x in itertools.product(models, genomes, chroms)]

    idx = int(sys.argv[1])
    vals = combinations[idx]

    params = vals[0]
    assembly = vals[1]
    chrom = vals[2]

    model_filename = params[0]
    protein = params[1]
    width = params[2]
    core = params[3]
    kmers_list = params[4]
    transform = params[5]


    # predict_genome.py
    #usage: predict_genome.py [-h] -g GenomeFile [--chroms [Chroms [Chroms ...]]]
    #                         -m ModelFile -c Core -w Width -k Kmers [Kmers ...]
    #                         [-i] [-t] -o OutputFile

    genome_file = '{}/{}.fa'.format(genome_files_dir, assembly)
    model_file = '{}/{}'.format(model_files_dir, model_filename)
    output_dir = output_dir_name(output_base, assembly, protein)
    output_file = output_file_name(output_dir, model_filename, chrom)

    # core set earlier
    # width set earlier

    # predict_genome
    command = ['python', 'predict_genome.py',
               '-g', genome_file, '--chroms', chrom,
               '-m', model_file, '-c', core,
               '-w', str(width), '-k']
    command.extend(kmers_list)
    if transform:
      command.append('-t')

    command.extend(['-o', output_file])

    try:
      os.makedirs(output_dir)
    except OSError as e:
      pass # Tried to check if not exists first, but when we schedule multiple simultaneous jobs, it fails.
    print ' '.join(command)

