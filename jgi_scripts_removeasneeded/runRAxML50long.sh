#! /bin/bash
#$ -cwd
#$ -r n
#$ -S /bin/bash
#$ -w e
#$ -pe pe_slots 8
#$ -P gentech-rnd.p
#$ -l h_rt=20:00:00

module load RAxML
raxmlHPC-PTHREADS-SSE3 -f a -x 12345 -p 12345 -# 50 -m PROTGAMMAJTT -T 8 -s $alnfile -n $outname
