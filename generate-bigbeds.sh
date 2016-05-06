#!/bin/bash
#
#SBATCH --mail-user=dan.leehr@duke.edu
#SBATCH --mail-type=FAIL

cd /home/dcl9/TrackHubGenerator
source env/bin/activate
srun run-json-jobs.sh /home/dcl9/tf-dna-sbatch/json-jobs/ /data/sciencesupport/tf-dna-predictions/results/bigbeds/
