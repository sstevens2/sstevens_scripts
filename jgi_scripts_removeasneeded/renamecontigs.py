#!/usr/common/usg/languages/python/2.7.4/bin/python

import sys, os

def usage():
	print "Usage: renamecontigs.py inputfile"

if len(sys.argv) !=2:
	usage()
	exit()

file=open(sys.argv[1], "rU")
lines=file.readlines()
file.close()
binname=sys.argv[1].split(".fa")[0]
output=open(binname+"_renamed.fa", "w")
output2=open(binname+"_contiglist.txt", "w")

for line in lines:
	if line.startswith(">") == True:
#		for new Mendota files
#		if binname.startswith("MEint") == True:
#			output.write(">"+binname+"_"+line.split("-")[1])
#			output2.write(line.split("-")[1])
#		if binname.startswith("Mendota") == True:		
#		for Mendota
#			output.write(">"+binname+"_"+line.split("-")[1].split(" ")[0]+"\n")
#			output2.write(line.split("-")[1].split(" ")[0]+"\n")
#		for TB
#		if binname.startswith("lake") == True:
#		if binname.startswith("TB") == True:
			output.write(">"+binname+"_"+line.split("_")[-1])
			output2.write(line.split("_")[-1])
	else:
		output.write(line)


output.close()
output2.close()


"""
#Old TB contig names
TBL_comb47_HYPODRAFT_10003780
TBL_comb48_EPIDRAFT_1000905
#Old ME contig names
contig-2344002956 5988 nucleotides
#new ME contig names
contig-205000428
"""
