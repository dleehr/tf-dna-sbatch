import predict_genome_wrapper as pgw
import os
import json

ORDERED_PROTEINS_THRESHOLDS = [
  {'protein':'E2F1', 'filter_threshold': 0.1933},
  {'protein':'E2F4', 'filter_threshold': 0.1620},
  {'protein':'ELK1', 'filter_threshold': 0.2244},
  {'protein':'ETS1', 'filter_threshold': 0.2128},
  {'protein':'HisMadMax', 'filter_threshold': 0.1837},
  {'protein':'HisMycMax', 'filter_threshold': 0.1619},
  {'protein':'E2F3', 'filter_threshold': 0.2762},
  {'protein':'GABPA', 'filter_threshold': 0.2888},
  {'protein':'HisMax', 'filter_threshold': 0.2386},
  {'protein':'Runx1', 'filter_threshold': 0.3061},
  {'protein':'Runx2', 'filter_threshold': 0.2711},
]

ORDERED_PROTEINS = [x['protein'] for x in ORDERED_PROTEINS_THRESHOLDS ]
FILTER_THRESHOLDS = { x['protein']: x['filter_threshold'] for x in ORDERED_PROTEINS_THRESHOLDS }

def make_job_dict(input_file_paths, filter_threshold, assembly, intermediate_output_file_name, output_bigbed_file_name):
    job = dict()
    input_files = list()
    for path in input_file_paths:
        input_files.append({'class':'File', 'path': path})
    job['input_files'] = input_files
    job['filter_threshold'] = filter_threshold
    job['assembly'] = assembly
    job['intermediate_output_file_name'] = intermediate_output_file_name
    job['output_bigbed_file_name'] = output_bigbed_file_name
    return job


def main(start_protein_number):
    for assembly in pgw.genomes:
        protein_number = start_protein_number
        for protein in ORDERED_PROTEINS:
            # One set of input files per model
            formatted_protein_number = '{0:04d}'.format(protein_number)
            input_file_paths = list()
            models = [model for model in pgw.models if model[1] == protein]
            for model in models:
                model_filename = model[0]
                base_model_filename = os.path.splitext(model_filename)[0]
                output_dir = pgw.output_dir_name(pgw.output_base, assembly, protein)
                for chrom in pgw.chroms:
                    input_file_paths.append(pgw.output_file_name(output_dir, os.path.basename(model_filename), chrom))
            # Now we have a list of source filenames
            filter_threshold = FILTER_THRESHOLDS[protein]
            intermediate_output_file_name = '{}-{}-{}.bed'.format(assembly, formatted_protein_number, protein)
            output_bigbed_file_name = '{}-{}-{}.bb'.format(assembly, formatted_protein_number, protein)
            job_file_name = 'json-jobs/' + os.path.splitext(intermediate_output_file_name)[0] + '.json'
            job_dict = make_job_dict(input_file_paths, filter_threshold, assembly, intermediate_output_file_name, output_bigbed_file_name)
            print 'writing to ', job_file_name
            with open(job_file_name, 'w') as f:
                json.dump(job_dict, f, indent=2)
            protein_number += 1


if __name__ == '__main__':
    protein_number = 3
    main(protein_number)
