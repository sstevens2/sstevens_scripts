#!/usr/bin/python

import sys, csv, os

"""contig_len.py: Takes a fasta file and returns each entry's name and sequence length in a txt file"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: contig_len.py fastafile"
	sys.exit(2)

if len(sys.argv) != 2:
	usage()
	exit()

filename=sys.argv[1]

output_name=filename.split("/")[-1].split(".")[0]+".len"
print "Working on "+ output_name
fastafile=open(filename, "rU")
fasta=fastafile.read()
fastafile.close()
reads=fasta.split(">")
reads.pop(0)
outputfile=open(output_name, "w")
for read in reads:
	rsplit=read.split("\n")
	seq="".join(rsplit[1:-1])
	outputfile.write(rsplit[0]+"\t"+str(len(seq))+"\n")
outputfile.close()
