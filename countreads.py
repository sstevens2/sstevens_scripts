#!/usr/bin/env python

import sys, os

"""countreads.py counts the number of reads in a fasta file by looking for the number of >
"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"


def usage():
	print "Usage: countreads.py fastafile"


if len(sys.argv) != 2:
	usage()
	exit()

fastafile=open(sys.argv[1], 'rt')
fasta=fastafile.read()

print fasta.count(">")
outname=sys.argv[1].split("/")[-1]+'.reads'
with open(outname, 'wt') as out:
	out.write(sys.argv[1].split("/")[-1]+"\t"+str(fasta.count(">"))+"\n")