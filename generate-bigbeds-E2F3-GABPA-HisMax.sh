#!/bin/bash
#
#SBATCH --mail-user=dan.leehr@duke.edu
#SBATCH --mail-type=FAIL

cd /home/dcl9/TrackHubGenerator
module load Anaconda/2.1.0-fasrc01
source activate env
srun run-json-jobs-no-resize.sh /home/dcl9/tf-dna-sbatch/json-jobs-2016-08-19/ /data/sciencesupport/tf-dna-predictions/results/bigbeds/
