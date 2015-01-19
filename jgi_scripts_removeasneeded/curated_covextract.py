#!/usr/common/usg/languages/python/2.7.4/bin/python

import sys, os, pickle

"""curated_covextract.py : pulls out the contigs for only curated genomes and writes
	to new file for each curated genome.  one off script, unless modified"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: ccurated_covextract.py <curated_dir> <cov_file>"

if len(sys.argv) != 3:
	usage()
	sys.exit(2)

curdirlist=os.listdir(sys.argv[1])
curlist=[]
for file in curdirlist:
	if file.endswith('.contigs.txt'):
		curlist.append(file)

covfile=open(sys.argv[2], 'rU')
covdata=covfile.readlines()

for file in curlist:
	datafile=open(sys.argv[1]+file, 'rU')
	data=datafile.readlines()
#	print data
	#create outputfile
	output=open(file.split('.')[0]+'_contigcov.txt', 'w')
	output.write(covdata[0])
	for contig in data:
		for line in covdata:
			contigname=contig.split('\n')[0]
			linename=line.split('\t')[0]
			if contigname==linename:
#				print contigname, linename
				output.write(line)


#/global/dna/projectdirs/RD/singlecell/Projects/timeseries/bins/curated/tb_hyp/