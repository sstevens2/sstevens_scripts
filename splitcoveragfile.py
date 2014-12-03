#!/usr/bin/python

import sys, csv, os

"""splitcoveragefile.py This will take the coverage file that from Matt Bendall that has the coverage
	across many time points for each contigs in many genomes, it will split up the data for the next
	steps in the process(with R....hopefully)"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: splitcoveragfile.py inputfile"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

#covfile=sys.argv[1]
covfile=open(sys.argv[1], 'rU')
cov=covfile.readlines()
covend=sys.argv[1].split('.')[1]

gnlist=[]
glist=[]
for line in cov:
	contig=line.split('\t')[0]
	gname=contig.split('|')[0]
	if gname not in glist:
		glist.append(gname)
		gnlist.append([])
	index=glist.index(gname)
	gnlist[index].append(line)

for list in gnlist:
	index=gnlist.index(list)
	name=glist[index]
	if name=='contig':
		continue
	output=open(name+'.'+covend+'.txt','w')
	output.write(gnlist[0][0])
	for line in list:
		output.write(line)
	output.close()