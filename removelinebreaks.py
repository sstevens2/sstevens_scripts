#!/usr/bin/env python

import sys

def usage():
	print "Usage: removelinebreaks.py [fastalistofseqs.fna] [newfastafile.fasta]"

if len(sys.argv) != 3:
	usage()
	exit()

outputfile = open(sys.argv[2], "w")
fastafile = open(sys.argv[1], "rU")

for line in  fastafile.readlines():
	if line.startswith('>'):
		outputfile.write("\n"+line)
	else:
		outputfile.write(line.split("\n")[0])
		
fastafile.close()
outputfile.close()