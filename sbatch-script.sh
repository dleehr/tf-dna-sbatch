#!/bin/bash
#
#SBATCH --mail-user=dan.leehr@duke.edu
#SBATCH --mail-type=FAIL
#SBATCH --array=0-143
#SBATCH --cpu=1
#SBATCH --mem=16g

# 1x2x24x3 = 144
TASKS=$(python -c "import itertools;genomes='hg19'.split();proteins='E2F1 E2F4'.split();chroms='chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chr19 chr20 chr21 chr22 chrX chrY'.split();cores='CCGC GCGC GCGG'.split();print ' '.join(['_'.join(x) for x in list(itertools.product(genomes, proteins, chroms, cores))])")
TASKS_ARRAY=(${TASKS// / })

TASK=${TASKS_ARRAY[$SLURM_ARRAY_TASK_ID]}

TASK_ARRAY=(${TASK//_/ })
GENOME=${TASK_ARRAY[0]}
PROTEIN=${TASK_ARRAY[1]}
CHROM=${TASK_ARRAY[2]}
CORE=${TASK_ARRAY[3]}

echo "Queueing job for ${GENOME}, ${PROTEIN}, ${CHROM}, ${CORE}"

GENOME_FILE="/data/sciencesupport/tf-dna-predictions/genomes/${GENOME}.fa"
MODEL_FILE="/data/sciencesupport/tf-dna-predictions/models/${PROTEIN}-bestSVR.model"
OUTPUT_FILE="/data/sciencesupport/tf-dna-predictions/results/${GENOME}-${PROTEIN}-${CHROM}-${CORE}-predictions.bed"

source /home/dcl9/SVR_models/env/bin/activate
  echo /home/dcl9/SVR_models/predict_genome.py \
  -g $GENOME_FILE \
  -m $MODEL_FILE \
  --chroms $CHROM \
  -c $CORE \
  -w 36 \
  -k 3 \
  -i \
  -o $OUTPUT_FILE
PYTHONPATH=/home/dcl9/libsvm/libsvm-321/python \
  srun python /home/dcl9/SVR_models/predict_genome.py \
  -g $GENOME_FILE \
  -m $MODEL_FILE \
  --chroms $CHROM \
  -c $CORE \
  -w 36 \
  -k 3 \
  -i \
  -o $OUTPUT_FILE
