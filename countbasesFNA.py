#!/usr/bin/python

import sys

"""outbasesFNA.py counts the number of bases that are in any fasta file, should also work on aa
"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: outbasesFNA.py inputFasta"
	print "outbasesFNA.py counts the number of bases that are in any fasta file, should also work on aa"

if len(sys.argv) != 2:
	usage()
	exit()

fastafile=open(sys.argv[1], "rU")
fasta=fastafile.readlines()

count=0
for line in fasta:
	if not line.startswith(">"):
		count=count+(len(line)-1)

outname=sys.argv[1]+'.len'
with open(outname, 'wt') as out:
	out.write(sys.argv[1]+"\t"+str(count)+'\n')
	print sys.argv[1]+"\t"+str(count)