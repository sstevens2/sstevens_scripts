#!/usr/bin/env python

import sys, os, Bio, re
from Bio import SeqIO

def usage():
	print "Usage: gbk2faafna.py [genbankfile] [aafilename.faa] [nucgenefile.fna]"

if len(sys.argv) != 4:
	usage()
	exit()
	
inputfile=open(sys.argv[1], "rU")
aaoutput=open(sys.argv[2], "w")
nucoutput=open(sys.argv[3], "w")
records = list(SeqIO.parse(inputfile, "genbank"))
inputfile.close()
output_record= []
for record in records:
	print record
	for feature in record.features:
		match = re.match("rRNA", feature.type)
		if match != None:
			print feature
aaoutput.close()
nucoutput.close()
