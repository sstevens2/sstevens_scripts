#!/usr/bin/python

import sys, os, csv

"""rm_rRNAhits.py: takes a list of files to remove hits from and a list of the
	contig and coordinates that hits should be removed from"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: rm_rRNAhits.py blastfilelist toremovelist"
	sys.exit(2)

if len(sys.argv) != 3:
	usage()
	exit()

blastfile=open(sys.argv[1], 'rU')
blastlist=blastfile.readlines()
tormfile=open(sys.argv[2], 'rU')
torm=tormfile.readlines()
torm_contigs=[]
for line in torm:
	torm_contigs.append(line.split('\t')[0])

for file in blastlist:
	file=file.split('\n')[0]
	blast=open(file, 'rU')
	blast=blast.readlines()
	output=open(file+".norrna",'w')
	for line in blast:
		line_s=line.split('\t')
		hstart=int(line_s[8])
		hend=int(line_s[9])
		name=line_s[1]
		if name in torm_contigs:
			match=""
			for row in torm:
				row_s=row.split('\n')[0].split('\t')
				if row_s[0]==name:
					rstart=int(row_s[1])
					rend=int(row_s[2])
					if (rstart < hstart < rend) or (rstart < hend < rend):
						break
					else:
						output.write(line)
				else:
					continue
		else:
			output.write(line)
	output.close()