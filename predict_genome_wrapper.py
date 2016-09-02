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

# Models added 2016-08-02

e2f3_files = '''E2F/E2F3_250nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGC_1a2a3mer_format.model
E2F/E2F3_250nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGG_1a2a3mer_format.model'''

gabpa_files = '''ETS/GABPA_100nM_Bound_filtered_normalized_transformed_20bp_GGAA_1a2a3mer_format.model
ETS/GABPA_100nM_Bound_filtered_normalized_transformed_20bp_GGAT_1a2a3mer_format.model'''

hismax_files = '''bHLH/HisMax_Bound_filtered_normalized_logistic_transformed_20bp_CACATG_1a2a3mer_format.model
bHLH/HisMax_Bound_filtered_normalized_logistic_transformed_20bp_CACGAG_1a2a3mer_format.model
bHLH/HisMax_Bound_filtered_normalized_logistic_transformed_20bp_CACGCG_1a2a3mer_format.model
bHLH/HisMax_Bound_filtered_normalized_logistic_transformed_20bp_CACGTG_1a2a3mer_format.model
bHLH/HisMax_Bound_filtered_normalized_logistic_transformed_20bp_CATGCG_1a2a3mer_format.model'''

# Models added 2016-09-02

runx_files = '''RUNX/Runx1_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GAGGT_1a2a3mer_format.model
RUNX/Runx1_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGGC_1a2a3mer_format.model
RUNX/Runx1_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGGG_1a2a3mer_format.model
RUNX/Runx1_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGGT_1a2a3mer_format.model
RUNX/Runx1_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GTGGC_1a2a3mer_format.model
RUNX/Runx1_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GTGGG_1a2a3mer_format.model
RUNX/Runx1_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GTGGT_1a2a3mer_format.model
RUNX/Runx2_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GAGGT_1a2a3mer_format.model
RUNX/Runx2_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGGC_1a2a3mer_format.model
RUNX/Runx2_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGGG_1a2a3mer_format.model
RUNX/Runx2_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GCGGT_1a2a3mer_format.model
RUNX/Runx2_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GTGGC_1a2a3mer_format.model
RUNX/Runx2_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GTGGG_1a2a3mer_format.model
RUNX/Runx2_10nM_Bound_filtered_normalized_logistic_transformed_20bp_GTGGT_1a2a3mer_format.model'''

def extract_width_int(width_string):
    return int(''.join([x for x in width_string if x.isdigit()]))

# Functions to parsae the model file names
def parse_e2f(f):
    f = f.split('/')[1]
    components = f.split('_')
    protein = components[0]
    width = extract_width_int(components[7])
    core = components[8]
    kmers = components[9].replace('mer','').split('a')
    return [protein, width, core, kmers, True]

def parse_elkets(f):
    f = f.split('/')[1]
    components = f.split('_')
    protein = components[0]
    width = extract_width_int(components[6])
    core = components[7]
    kmers = components[8].replace('mer','').split('a')
    return [protein, width, core, kmers, True]

def parse_hismadmax(f):
    f = f.split('/')[1]
    components = f.split('_')
    protein = components[0]
    width = extract_width_int(components[5])
    core = components[6]
    kmers = components[7].replace('mer','').split('a')
    return [protein, width, core, kmers, True]

def parse_hismax(f):
    f = f.split('/')[1]
    components = f.split('_')
    protein = components[0]
    width = extract_width_int(components[6])
    core = components[7]
    kmers = components[8].replace('mer','').split('a')
    return [protein, width, core, kmers, True]

def parse_runx(f):
    f = f.split('/')[1]
    components = f.split('_')
    protein = components[0]
    width = extract_width_int(components[7])
    core = components[8]
    kmers = components[9].replace('mer','').split('a')
    return [protein, width, core, kmers, True]

models = list()
for f in e2f_files.splitlines():
    models.append([f] + parse_e2f(f))
for f in elkets_files.splitlines():
    models.append([f] + parse_elkets(f))
for f in hismadmax_files.splitlines():
    models.append([f] + parse_hismadmax(f))
# Adding models 2016-08-02
for f in e2f3_files.splitlines():
    models.append([f] + parse_e2f(f))
for f in gabpa_files.splitlines():
    models.append([f] + parse_elkets(f))
for f in hismax_files.splitlines():
    models.append([f] + parse_hismax(f))
for f in runx_files.splitlines():
    models.append([f] + parse_runx(f))

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
    if len(sys.argv) == 1:
        print 'Usage: {} <0-{}>'.format(sys.argv[0], len(combinations) -1)
        sys.exit(1)

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

    genome_file = '{}/{}.fa'.format(genome_files_dir, assembly)
    model_file = '{}/{}'.format(model_files_dir, model_filename)
    output_dir = output_dir_name(output_base, assembly, protein)
    output_file = output_file_name(output_dir, os.path.basename(model_filename), chrom)

    # core set earlier
    # width set earlier

    # predict_tf_binding
    command = ['python', 'predict_tf_binding.py',
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

