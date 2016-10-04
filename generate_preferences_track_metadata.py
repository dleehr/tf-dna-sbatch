import predict_genome_wrapper as pgw
import os
from generate_preference_jobs import PREFERENCE_PAIRS, MODEL_KEYS,  make_pair_base_filename, get_protein_number, FILTER_THRESHOLDS

import yaml

def write_yaml(file_name):
    metadata_dicts = []
    for assembly in pgw.genomes:
      for pair in PREFERENCE_PAIRS:
        proteins = [p for p in pair['proteins']] # ensures yaml uses literals
        serial_numbers = [get_protein_number(p) for p in proteins]
        filter_thresholds = [FILTER_THRESHOLDS[p] for p in proteins]
        track_filename = make_pair_base_filename(assembly, proteins) + '.bb'
        track_name = '{}_vs_{}'.format(proteins[0], proteins[1])
        author_identifier = 'NS'
        # Pull out the model details for the first protein
        model_key = MODEL_KEYS[proteins[0]]
        models = [model for model in pgw.models if model[1] == model_key]
        # models is a list of files and their decoded parameters.
        cores = [model[3] for model in models]
        model = models[0]
        core_start = model[6]
        family = model[7]
        metadata = dict(assembly=assembly, track_filename=track_filename, track_name=track_name,author_identifier=author_identifier, proteins=proteins, cores=cores, core_start=core_start, family=family, serial_numbers=serial_numbers, filter_thresholds=filter_thresholds)
        metadata_dicts.append(metadata)
    with open(file_name, 'w') as f:
        f.write( yaml.dump(metadata_dicts, default_flow_style=False) )

if __name__ == '__main__':
    write_yaml('tracks-preferences.yaml')
