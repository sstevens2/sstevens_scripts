#!/usr/bin/python

import sys, os, Bio

"""gbk_extractGeneInfo.py The program takes a genbank file and then pulls out the
	locus tag, start, stop, nucleotide sequence, and protein sequence for each gene"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: gbk_extractGeneInfo.py inputfile"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

inputfile=sys.argv[1]
output=open(sys.argv[1].split(".gb")[0]+".tsv", "w")
outputfaa=open(sys.argv[1].split(".gb")[0]+".faa", "w")

from Bio import SeqIO
file=open(inputfile, "rU")
records = SeqIO.read(file, "genbank")
output.write("locus_tag\tstart\tstop\tstrand\tprot_seq\tprot_len\n")
file.close()
for record in records.features:
	if record.type == 'CDS':
		output.write(record.qualifiers['locus_tag'][0]+"\t")
		output.write(str(record.location.nofuzzy_start)+"\t")
		output.write(str(record.location.nofuzzy_end)+"\t")
		output.write(str(record.strand)+"\t")
		output.write(record.qualifiers['translation'][0]+"\t")
		output.write(str(len(record.qualifiers['translation'][0]))+"\n")
		outputfaa.write(">"+record.qualifiers['locus_tag'][0]+"\n")
		outputfaa.write(record.qualifiers['translation'][0]+"\n")
output.close()
outputfaa.close()