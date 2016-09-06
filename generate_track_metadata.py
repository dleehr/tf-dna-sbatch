import predict_genome_wrapper as pgw
import os
from generate_json_jobs import FILTER_THRESHOLDS, ORDERED_PROTEINS
import yaml

def write_yaml(file_name):
    metadata_dicts = []
    for assembly in pgw.genomes:
        model_number = 1
        # Tracks from JS
        for protein in ['E2F1', 'E2F4']:
            serial_number = '{0:04d}'.format(model_number)
            # E2F1-bestSVR.model.bb
            model_filename = '{}-bestSVR.model'.format(protein)
            # hg38-0001-E2F1-E2F1-bestSVR.model.bb
            track_filename = '{}-{}-{}-{}.bb'.format(assembly, serial_number, protein, model_filename)
            author_identifier = 'JS'
            filter_threshold = 0.207
            cores = ['CCGC','GCGC','GCGG']
            kmers = [3]
            width = 36
            slope_intercept = True
            transform = False
            track_name = '{}_{}({})'.format(protein, serial_number, author_identifier)
            metadata = dict(assembly=assembly, track_filename=track_filename, track_name=track_name, model_filenames=[model_filename], author_identifier=author_identifier, serial_number=serial_number, filter_threshold=filter_threshold, protein=protein, cores=cores, kmers=kmers, width=width, slope_intercept=slope_intercept, transform=transform, core_start=None)
            metadata_dicts.append(metadata)
            model_number += 1
        # Tracks from NS - one track per protein. Protein, core, width, kmers encoded in the model filename
        for protein in ORDERED_PROTEINS:
            # One set of input files per model
            serial_number = '{0:04d}'.format(model_number)
            models = [model for model in pgw.models if model[1] == protein]
            model_filenames = [os.path.basename(model[0]) for model in models]
            author_identifier = 'NS'
            filter_threshold = FILTER_THRESHOLDS[protein]
            track_filename = '{}-{}-{}.bb'.format(assembly, serial_number, protein)
            track_name = '{}_{}({})'.format(protein, serial_number, author_identifier)
            width = int(model[2])
            cores = [model[3] for model in models]
            kmers = [int(x) for x in models[0][4]] #kmers must be consistent for all models on a protein
            slope_intercept = False
            # Assign to literal values so that yaml doesn't use references
            if model[4]:
              transform = True
            else:
              transform = False
            core_start = model[6]
            metadata = dict(assembly=assembly, track_filename=track_filename, track_name=track_name, model_filenames=model_filenames, author_identifier=author_identifier, serial_number=serial_number, filter_threshold=filter_threshold, protein=protein, cores=cores, kmers=kmers, width=width, slope_intercept=slope_intercept, transform=transform, core_start=core_start)
            metadata_dicts.append(metadata)
            model_number += 1
    with open(file_name, 'w') as f:
        f.write( yaml.dump(metadata_dicts, default_flow_style=False) )

if __name__ == '__main__':
    write_yaml('tracks.yaml')




