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
	#print record
	for feature in record.features:
		if feature.type == 'CDS':
			assert len(record.seq[feature.location.nofuzzy_start:feature.location.nofuzzy_end]) % 3 == 0
			print len(record.seq[feature.location.nofuzzy_start:feature.location.nofuzzy_end])/3
			print len(feature.qualifiers['translation'][0])
			assert len(record.seq[feature.location.nofuzzy_start:feature.location.nofuzzy_end])/3 == len(feature.qualifiers['translation'][0])
aaoutput.close()
nucoutput.close()
