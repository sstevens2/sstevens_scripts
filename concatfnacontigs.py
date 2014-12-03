#!/usr/bin/env python

import sys, os

def usage():
	print "Usage: concatfnacontigs.py pathtofiles"


if len(sys.argv) != 2:
	usage()
	exit()

path2files = sys.argv[1]

for file in os.listdir(path2files):
		print file.split(".")[1]
		fastafile = open(str(file), "rU")
		fasta = fastafile.readlines()
		SAGname=file.split(".")[0]
		outname = SAGname+"_cat.fna"
		outfile = open(outname, "w")
		outfile.write(">"+SAGname+"\n")
		for line in fasta:
			if not line.startswith(">"):
				outfile.write(line)
		fastafile.close()
		outfile.close()
			
	