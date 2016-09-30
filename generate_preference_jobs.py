import os
import json
import itertools

from predict_genome_wrapper import output_base as BEDFILES_BASE
from predict_genome_wrapper import output_file_name as bedfile_name
from predict_genome_wrapper import models as MODELS
from predict_genome_wrapper import genomes, chroms, output_dir_name
from generate_json_jobs import FILTER_THRESHOLDS, MODEL_KEYS, ORDERED_PROTEINS

# what are the pairs we want to run
PREFERENCE_PAIRS = [
  {'family' : 'ETS', 'proteins': ('Elk1','Ets1',) },
  {'family': 'E2F', 'proteins': ('E2f1','E2f4',) },
  {'family': 'E2F', 'proteins': ('E2f1','E2f3',) },
  {'family' : 'bHLH', 'proteins': ('Mad1','c-Myc') },
  {'family' : 'RUNX', 'proteins': ('Runx1','Runx2') },
]

combinations = [x for x in itertools.product(PREFERENCE_PAIRS, genomes, chroms)]

def get_protein_number(protein):
  index = ORDERED_PROTEINS.index(protein)
  return '{0:04d}'.format(index + 1)


def get_model_files(model_key):
  # May need to use the mapped protein names. in MODELS they are uppercase
  matching_models = [m for m in MODELS if m[1] == model_key]
  return [os.path.basename(m[0]) for m in matching_models]


def make_files_list(assembly, protein):
  # Need to make an ordered list of files based on the models
  files = list()
  model_files = get_model_files(MODEL_KEYS[protein])
  for model_filename in model_files:
    for chrom in chroms:
      bedfiles_dir = output_dir_name(BEDFILES_BASE, assembly, MODEL_KEYS[protein])
      bedfile = bedfile_name(bedfiles_dir, os.path.basename(model_filename), chrom)
      files.append(bedfile)
  files = [{'path':f,'class':'File'} for f in files]
  return files

def make_pair_base_filename(assembly, proteins):
  # hg19_0004_Elk1_0005_Ets1.bb
  protein_numbers = [get_protein_number(protein) for protein in proteins]
  return '{}_{}_{}_{}_{}'.format(assembly, protein_numbers[0], proteins[0], protein_numbers[1], proteins[1])


for assembly in genomes:
  for pair in PREFERENCE_PAIRS:
    proteins = pair['proteins']
    pair_base_filename = make_pair_base_filename(assembly, proteins)
    job_dict = dict(assembly=assembly, output_bigbed_file_name=pair_base_filename + '.bb', intermediate_output_file_name=pair_base_filename + '.bed')
    for idx, protein in enumerate(proteins):
      tf_key = 'tf' + str(idx + 1) # tf1, tf2
      thresh_key = tf_key + '_threshold'
      bed_files_key = tf_key + '_bed_files'
      job_dict[tf_key] = protein
      job_dict[thresh_key] = FILTER_THRESHOLDS[protein]
      job_dict[bed_files_key] = make_files_list(assembly,protein)
    json_file_name = 'json-jobs/{}.json'.format(pair_base_filename)
    with open(json_file_name, 'w') as j:
      json.dump(job_dict, j, indent=2)
