#!/usr/bin/env python

import sys, os, Bio
from Bio import SeqIO

def usage():
	print "Usage: gcContent.py [fastalistofseqs.fna] [outputfilname.tsv]"

if len(sys.argv) != 3:
	usage()
	exit()

outputfile = open(sys.argv[2], "w")
fastafile = open(sys.argv[1], "rU")
records = list(SeqIO.parse(fastafile, "fasta"))
fastafile.close()
outputfile.write("gene_name\tgene_description\tgene_seq\tgene_length\tgene_gcContent_percent\tA_count\tT_count\tC_count\tG_count\n")

for gene in records:
	Acount = gene.seq.count('A')
	Tcount = gene.seq.count('T')
	Gcount = gene.seq.count('G')
	Ccount = gene.seq.count('C')
	length = len(gene.seq)
	gcpercent = float(Gcount+Ccount) / length
	outputline = str(gene.name+"\t"+gene.description+"\t"+gene.seq+"\t"+str(length)+"\t"+str(gcpercent)+"\t"+str(Acount)+"\t"+str(Tcount)+"\t"+str(Ccount)+"\t"+str(Gcount)+"\n")
	outputfile.write(outputline)
	
outputfile.close()
