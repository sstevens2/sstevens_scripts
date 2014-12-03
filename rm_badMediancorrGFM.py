#!/usr/bin/python

import sys, csv

"""rm_badMediancorrGFM.py  - this program cuts out those contigs with a
	low correlation(below cutoffcor) from the coverage file of a GFM.
	must have GFM.tsv.corr.tsv to correspond with GFM.tsv that is the
	coveragefile.tsv input. """

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: rmv_badMediancorrGFM.py coveragefile.tsv cutoffcor"

if len(sys.argv) != 3:
	usage()
	sys.exit(2)

covfile=open(sys.argv[1], "rU")
corrfile=open(sys.argv[1]+".corr.tsv", "rU")
corin=corrfile.readlines()
covin=covfile.readlines()
corrfile.close()
covfile.close()
cutcor=float(sys.argv[2])

output=open(sys.argv[1]+".corrcut"+sys.argv[2]+".tsv", "w")
index=0
for row in covin:
	if index==0:
		output.write(row)
		index+=1
	else:
		actcor=float(corin[index].split("\t")[1])
		if actcor > cutcor:
#			print row, actcor
			output.write(row)
		index+=1
output.close()
			