#!/bin/bash
#
#SBATCH --mail-user=dan.leehr@duke.edu
#SBATCH --mail-type=FAIL

cd /home/dcl9/TrackHubGenerator
module load Anaconda/2.1.0-fasrc01
srun run-json-jobs-no-filter.sh /home/dcl9/tf-dna-sbatch/json-jobs-2017-03-02-predictions-no-filter/ /data/sciencesupport/tf-dna-predictions/results/bigbeds-no-filter/
