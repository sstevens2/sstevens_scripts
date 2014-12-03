#! /bin/bash
#$ -cwd
#$ -r n
#$ -S /bin/bash
#$ -w e
#$ -pe pe_slots 8
#$ -P gentech-rnd.p

ANI=/global/projectb/projectdirs/microbial/single_cell_genomics/scripts/averageNucleotideIdentity.pl
fastafile=GFM_all.faa
perl $ANI -threads 8 -ANI $outfile -query $fastafile -subject $fastafile		