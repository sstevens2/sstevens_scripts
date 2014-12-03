#!/usr/bin/env python

import sys

def usage():
	print("Usage: concatGenes2genome.py [fnainputfile] [fnaoutputfilename] ")
	print("Takes a fasta file with many sequences and concatenates them all into one big sequence.  Retains the naming info for the first seq in the file, in order to make it compatible with calc_codonbias.py.")

if len(sys.argv) != 3:
	usage()
	exit()

inputfile = open(sys.argv[1], "rU")
fnafile = inputfile.readlines()
inputfile.close()
outputfile = open(sys.argv[2], "w")

fullgenome = ""
for line in fnafile:
    if line.startswith(">"):
        print(line)
    else:
        fullgenome = fullgenome + line.split("\n")[0]
#outputfile.write(">" + (sys.argv[2].split(".fna")[0]) + "\n")
outputfile.write(fnafile[0])
outputfile.write(fullgenome)
outputfile.close()
