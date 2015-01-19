#!/usr/bin/python

import sys, os, pandas

"""norm_genecounts.py : this program is to normalize each column(metagenome) by
	the number of hits that SAG had in that metagenome"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: norm_genecounts.py <genecovfile> <hitcounts>"

if len(sys.argv) != 3:
	usage()
	sys.exit(2)

gencovfile=open(sys.argv[1], 'rU')
hitsfile=open(sys.argv[2], 'rU')
hits=hitsfile.readlines()

gencov=pandas.read_csv(gencovfile, sep='\t')
#print list(gencov.columns.values)
output=open(sys.argv[2].split('/')[-1].split('.')[0]+'gene_norm.tsv', 'w')
#output.write('locus_tag\t')

outlist=[]
for line in hits:
	templist=[]
	name=line.split('\t')[0]
	value=int(line.split('\t')[1])
	col=gencov[name]
	templist.append(name)
	for row in col:
		templist.append(row/value)
	outlist.append(templist)

locus_list=gencov['locus_tag']
#print locus_list[0]

for rindex in range(len(outlist[0])):
	if rindex==0:
		output.write('locus_tag\t')
	else:
		output.write(locus_list[rindex-1]+'\t')
	for cindex in range(len(outlist)):
		output.write(str(outlist[cindex][rindex])+'\t')
	output.write('\n')