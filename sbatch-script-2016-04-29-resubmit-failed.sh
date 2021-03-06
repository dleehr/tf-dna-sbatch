#!/bin/bash
#
#SBATCH --mail-user=dan.leehr@duke.edu
#SBATCH --mail-type=FAIL
#SBATCH --array=436,438,454,456,472,474,490,492,508,510,526,528
#SBATCH --cpu=1
#SBATCH --mem=16g

COMMAND=$(python predict_genome_wrapper.py $SLURM_ARRAY_TASK_ID)
cd /home/dcl9/SVR_models
echo $COMMAND
source /home/dcl9/SVR_models/env/bin/activate
PYTHONPATH=/home/dcl9/libsvm/libsvm-321/python \
  srun $COMMAND
