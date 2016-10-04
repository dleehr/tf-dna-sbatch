import predict_genome_wrapper as pgw
import os
from generate_json_jobs import ORDERED_PROTEINS_THRESHOLDS
import yaml

def write_yaml(file_name):
    metadata_dicts = []
    for assembly in pgw.genomes:
        model_number = 1
        # Tracks from NS - one track per protein. Protein, core, width, kmers encoded in the model filename
        for protein_dict in ORDERED_PROTEINS_THRESHOLDS:
            protein = protein_dict['protein']
            filter_threshold = protein_dict['filter_threshold']
            model_key = protein_dict['model_key']
            # One set of input files per model
            serial_number = '{0:04d}'.format(model_number)
            models = [model for model in pgw.models if model[1] == model_key]
            model_filenames = [os.path.basename(model[0]) for model in models]
            author_identifier = 'NS'
            track_filename = '{}_{}_{}.bb'.format(assembly, serial_number, protein)
            track_name = '{}_{}'.format(protein, serial_number)
            cores = [model[3] for model in models]
            kmers = [int(x) for x in models[0][4]] #kmers must be consistent for all models on a protein
            slope_intercept = False
            # Assign to literal values so that yaml doesn't use references
            model = models[0]
            width = int(model[2])
            if model[4]:
              transform = True
            else:
              transform = False
            core_start = model[6]
            family = model[7]
            metadata = dict(assembly=assembly, track_filename=track_filename, track_name=track_name, model_filenames=model_filenames, author_identifier=author_identifier, serial_number=serial_number, filter_threshold=filter_threshold, protein=protein, cores=cores, kmers=kmers, width=width, slope_intercept=slope_intercept, transform=transform, core_start=core_start, family=family)
            metadata_dicts.append(metadata)
            model_number += 1
    with open(file_name, 'w') as f:
        f.write( yaml.dump(metadata_dicts, default_flow_style=False) )

if __name__ == '__main__':
    write_yaml('tracks-predictions.yaml')
