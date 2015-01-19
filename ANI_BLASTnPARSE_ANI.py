#!/usr/bin/env python

import sys, os

def usage():
	print "Usage: ANI_BLASTnPARSE_ANI.py folder2faa"
	print "Runs for protein seqs"

if len(sys.argv) != 2:
	usage()
	exit()

path2faa= sys.argv[1]

#makedb for each
filelist=[]
for file in os.listdir(path2faa):
	if file.endswith(".faa"):
		filelist.append(file)
		os.system("makeblastdb -in " +path2faa+file+ " -out "+ path2faa+file.split(".faa")[0]+".db -dbtype prot")

#all v all blast
for file in filelist:
	for file2 in filelist:
		file1n=path2faa+file
		file2n=path2faa+file2.split(".faa")[0]+".db"
		outname=file1n.split(".faa")[0]+"v"+file2.split(".faa")[0]+".blast"
		print "BLASTING "+file+" v "+file2
		os.system("blastp -task blastp -query " + file1n+" -db "+file2n+" -out "+outname+" -evalue 0.001")
		os.system("filtersearchio5 -tophsp -qcoverage 50 -format 8 < " +outname+" > "+ outname+".tophsp.percqcov50")

for file in filelist:
	for file2 in filelist:
		file1n=path2faa+file.split(".faa")[0]+"v"+file2.split(".faa")[0]+".blast.tophsp.percqcov50"
		file2n=path2faa+file2.split(".faa")[0]+"v"+file.split(".faa")[0]+".blast.tophsp.percqcov50"
		os.system("perl ~/Programs/reciprocal_blast_hit_parsing2.pl -i1 " + file1n+" -i2 " +file2n+" -o " + path2faa+file.split(".faa")[0]+"v"+file2.split(".faa")[0]+".rbb")
