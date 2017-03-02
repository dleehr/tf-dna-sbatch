#!/bin/bash
#
#SBATCH --mail-user=dan.leehr@duke.edu
#SBATCH --mail-type=FAIL
#SBATCH --mem=16g

module load Anaconda/2.1.0-fasrc01
module load R/3.2.2-fasrc03
export PATH=$PATH:/home/dcl9/predict-tf-preference
cd /home/dcl9/TrackHubGenerator
srun run-preference-json-jobs.sh /home/dcl9/tf-dna-sbatch/json-jobs-2017-03-02-preferences-no-filter/ /data/sciencesupport/tf-dna-preferences/results/bigbeds/
