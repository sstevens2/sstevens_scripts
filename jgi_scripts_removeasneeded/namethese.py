#!/usr/bin/python python

#temp program to name stupid GFM for GOLD

import sys, os

def usage():
	print "Usage: namethese.py infile outfile"

if len(sys.argv) !=3:
	usage()
	exit()
	
inputfile = open(sys.argv[1], "rU")
file = inputfile.read()
inputfile.close()
outputfile = open(sys.argv[2], "w")

for line in file.split("\n"):
	outputfile.write(line)
	gname=line.split("\t")[2].split(" ")[-1]
	gname2=gname.split("_")[0]+gname.split("_")[1]
	if line.split("\t")[0] != ('VIRUSES' or "EUKARYOTA" or "NEMATODA"):
		outputfile.write(line.split("\t")[0] + " bacterium "+ gname2+"\n")
	if line.split("\t")[0] == 'VIRUSES':
		outputfile.write("virus "+ gname2+"\n")
	if line.split("\t")[0] == ("EUKARYOTA" or "NEMATODA"):
		outputfile.write(gname2+"\n")

outputfile.close()