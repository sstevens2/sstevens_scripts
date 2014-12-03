#! /bin/bash
#$ -cwd
#$ -r n
#$ -S /bin/bash
#$ -w e
#$ -pe pe_slots 8
#$ -P gentech-rnd.p

modlule load RAxML
raxmlHPC-PTHREADS-SSE3 -f a -x 12345 -p 12345 -# 100 -m PROTGAMMAJTT -T 8 -s $alnfile -n $outname