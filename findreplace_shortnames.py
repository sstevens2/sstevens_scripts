#!/usr/bin/python

import sys, os
"""findreplace_shortnames.py  replace the old contig names with the new contig names"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: findreplace_shortnames.py replacefile namekey"

if len(sys.argv) != 3:
	usage()
	sys.exit(2)

inputfile=open(sys.argv[1], 'rU')
namekey=open(sys.argv[2], 'rU')

input=inputfile.read()
namekey=namekey.readlines()

for line in namekey:
	old=line.split(' ')[0].split('>')[1]
	new=line.split('>')[-1].split('\n')[0]
	input=input.replace(old, new)

output=open(sys.argv[1].split('.')[0]+'_short.tsv','w')
output.write(input)
output.close()