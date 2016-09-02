#!/bin/bash
#
#SBATCH --mail-user=dan.leehr@duke.edu
#SBATCH --mail-type=FAIL
#SBATCH --array=1296-1967%24
#SBATCH --cpu=1
#SBATCH --mem=16g

COMMAND=$(python predict_genome_wrapper.py $SLURM_ARRAY_TASK_ID)
cd /home/dcl9/Predict-TF-Binding
echo $COMMAND
source /home/dcl9/Predict-TF-Binding/env/bin/activate
PYTHONPATH=/home/dcl9/libsvm/libsvm-321/python \
  srun $COMMAND
