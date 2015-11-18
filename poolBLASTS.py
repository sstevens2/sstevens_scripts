#!/usr/bin/python

import sys, os, csv, glob

"""poolBLASTS.py takes the metagenome metadata and a set of metagenome blasts, 
	and pools each month from the same year together."""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: poolBLASTS.py 'blastfilelist(glob)' metadatafile"
	sys.exit(2)

if len(sys.argv) != 3:
	usage()
	exit()

blastlist=glob.glob(sys.argv[1])
bsn=[] #blast sample names list
for line in blastlist:
	bsn.append(line.split('.')[0])

monthyear=[]
tocat=[]
with open(sys.argv[2], 'rU') as metafile:
	metadata=csv.reader(metafile, delimiter='\t')
	for row in metadata:
		name=row[0]
		year=row[5]
		month=row[6]
		if name in bsn:
			my=year+"_"+month
			if my not in monthyear:
				monthyear.append(my)
				tocat.append([])
			index=monthyear.index(my)
			tocat[index].append(name)

outfile=open('1metaMonYears.txt', 'w')
for group in tocat:
	command="cat"
	for meta in group:
		meta=meta+".len150-vs-14_acI_norrna_short.blast.len200"
		command=command+" "+meta
	outname=monthyear[tocat.index(group)]+".len150-vs-14_acI_norrna_short.blast.len200"
	command=command+"> "+outname
	if len(group) == 1:
		outfile.write(monthyear[tocat.index(group)]+'\t'+group[0]+'\n')
outfile.close()