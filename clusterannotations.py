#!/usr/bin/python

import sys, re

def usage():
	print "Usage: clusterannotations.py [clusters.tsv] [catgenelist] [clusterswanno.tsv]"

if len(sys.argv) != 4:
	usage()
	exit()

# DID NOT FINISH THIS, got frusterated
outputfile = open(sys.argv[3], "w")
genelistfile= open(sys.argv[2], "rU")
inputfile = open(sys.argv[1], "rU")

# Read in and sort the catgenelist file
lines = inputfile.readlines()
genelist= genelistfile.readlines()
sgenelist=[]
for line in genelist:
	temptable=[]
	for row in line.split("\n"):
		temptable.append(row.split("\t"))
	sgenelist.append(temptable)

#read in and sort the clusters file
linetabtable=[]
for line in lines:
	temptable=[]
	for tab in line.split("\t"):
		for item in tab.split("  "):
			for gene in sgenelist:
				match = re.match(gene[0][0],item)
				if match != None:
					print "Match"
		temptable.append(tab.split("  "))
	linetabtable.append(temptable)
print linetabtable[1]