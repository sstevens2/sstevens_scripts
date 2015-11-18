#!/usr/bin/python

import sys, os, glob

def usage():
	print "Usage: ANI_BLASTnPARSE_ANI.py 'glob4files'"
	print "Runs for protein seqs"

if len(sys.argv) != 2:
	usage()
	exit()

path2faa= os.path.split(sys.argv[1])[0]
filelist=glob.glob(sys.argv[1])

#all v all blast
for file in filelist:
	for file2 in filelist:
		file1n=os.path.split(file)[1]
		file2n=os.path.split(file2)[1]
		outname="{}v{}.blast".format(os.path.splitext(file1n)[0],os.path.splitext(file2n)[0])
		print("BLASTING {} v {}".format(file1n,file2n))
		os.system("blastp -task blastp -query {} -db {} -out {} -evalue 0.001".format(file,file2n+'.db',outname))
		print outname
		os.system("filtersearchio5 -tophsp -qcoverage 50 -format 8 < {0} > {0}.tophsp.percqcov50".format(outname))

for file in filelist:
	for file2 in filelist:
		file1n=path2faa+file.split(".faa")[0]+"v"+file2.split(".faa")[0]+".blast.tophsp.percqcov50"
		file2n=path2faa+file2.split(".faa")[0]+"v"+file.split(".faa")[0]+".blast.tophsp.percqcov50"
		os.system("perl ~/programs/reciprocal_blast_hit_parsing2 -i1 " + file1n+" -i2 " +file2n+" -o " + path2faa+file.split(".faa")[0]+"v"+file2.split(".faa")[0]+".rbb")
