#!/usr/bin/python

import os, sys

"""splitcoveragefile.py is a program that pulls out the contig names after from a fastafile 
	and saves them to a txt file. Txt file gets named, anything before '.fa' then '.txt' """

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: splitcoveragfile.py inputfile"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

file=sys.argv[1]

name=open(file, 'rU')
guts=name.readlines()
output=open(file.split('.fa')[0].split('/')[-1]+'.txt','w')
for line in guts:
	if line.startswith('>'):
		output.write(line.split('>')[1])
output.close()
