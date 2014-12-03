#!/usr/bin/env python

import sys, os

def usage():
	print "Usage: allfasta2fastq.py pathtofiles"
	print "Cuts name to whatever it is before the first '.'."

if len(sys.argv) != 2:
	usage()
	exit()

path2files=sys.argv[1]

for filename in os.listdir(path2files):
	if filename.split(".")[-1]=="fastq":
		os.system("fastQ2Fasta.pl -in "+filename+" -f "+filename.split(".")[0]+".fasta")
	
	
	