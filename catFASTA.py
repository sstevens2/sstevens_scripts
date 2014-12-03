#!/usr/bin/env python

import sys

def usage():
	print "Usage: catFASTA.py [fastaIN.fna] [fastaOUT.fasta]"

if len(sys.argv) != 3:
	usage()
	exit()

outputfile = open(sys.argv[2], "w")
fastafile = open(sys.argv[1], "rU")

outputfile.write(">" + sys.argv[1] + "_concatenated\n")

for line in  fastafile.readlines():
	if not line.startswith('>'):
		outputfile.write(line.split("\n")[0])
		
fastafile.close()
outputfile.close()