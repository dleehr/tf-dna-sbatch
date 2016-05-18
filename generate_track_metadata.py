import predict_genome_wrapper as pgw
from generate_json_jobs import FILTER_THRESHOLDS
import yaml

def make_metadata_dict(assembly, track_filename, model_filename, author_identifier, serial_number, filter_threshold, protein, cores, kmers, width, slope_intercept):
    m = dict()
    m['assembly'] = assembly
    m['track_filename'] = track_filename
    m['model_filename'] = model_filename
    m['author_identifier'] = author_identifier
    m['serial_number'] = serial_number
    m['filter_threshold'] = filter_threshold
    m['protein'] = protein
    m['cores'] = cores
    m['kmers'] = kmers
    m['width'] = width
    m['slope_intercept'] = slope_intercept
    return m


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
            metadata = make_metadata_dict(assembly, track_filename, model_filename, author_identifier, serial_number, filter_threshold, protein, cores, kmers, width, slope_intercept)
            metadata_dicts.append(metadata)
            model_number += 1
        # Tracks from NS - one track per model. Protein, core, width, kmers encoded in the model filename
        for model in pgw.models:
            serial_number = '{0:04d}'.format(model_number)
            model_filename = model[0]
            author_identifier = 'NS'
            protein = model[1]
            filter_threshold = FILTER_THRESHOLDS[protein]
            track_filename = '{}-{}-{}-{}.bb'.format(assembly, serial_number, protein, model_filename)
            width = model[2]
            cores = [model[3]]
            kmers = [int(x) for x in model[4]]
            slope_intercept = False
            metadata = make_metadata_dict(assembly, track_filename, model_filename, author_identifier, serial_number, filter_threshold, protein, cores, kmers, width, slope_intercept)
            metadata_dicts.append(metadata)
            model_number += 1
    with open(file_name, 'w') as f:
        f.write( yaml.dump(metadata_dicts, default_flow_style=False) )

if __name__ == '__main__':
    write_yaml('tracks.yaml')




