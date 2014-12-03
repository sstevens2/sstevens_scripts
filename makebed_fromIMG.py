#!/usr/bin/python

import sys, csv, os

"""makebed_fromIMG.py: takes the output from IMG download including
Gene ID	Locus Tag	Gene Product Name	Genome	Start Coord	End Coord	Strand	DNA Sequence Length (bp)	Amino Acid Sequence Length (aa)	Locus Type	Is Pseudogene	Is Obsolete	Is Partial Gene	Add Date	Is Public	Scaffold ID	Scaffold External Accession	Scaffold Name	Scaffold Length (bp)	Scaffold GC %	Scaffold Read Depth	COG	Pfam	Tigrfam	Enzyme	KO	IMG Term
	and makes it into a bed file which includes
Genome|Contig_in_old_name	Start	Stop	Locus_tag	Strand
	for only the CDS
	script is likely a one off, unless changed to parse the contig names differently
"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: makebed_fromIMG.py inputfile"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

output=open(sys.argv[1].split('.txt')[0]+'.bed','w')
with open(sys.argv[1], 'rb') as infile:
	inlist=csv.reader(infile, delimiter='\t')
	for row in inlist:
		if row[9]=='CDS':
			locustag, start, end, strand=row[1], row[4], row[5], row[6]
			contig=row[16].split('TH01379_')[-1].split('.')[0]
			genome='TH01379'
			output.write(genome+'|'+contig+'\t'+start+'\t'+end+'\t'+locustag+'\t.\t'+strand+'\n')
output.close()