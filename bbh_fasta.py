#!/usr/bin/python
#Sarah Stevens
#sstevens2@wisc.edu

import sys, os

#print this if not right number of input
def usage():
	print "Usage: bbh_fasta.py bbhblastfile fastafile"
	print "blast file needs to be in outfmt 6"

#check if right number of inputs
if len(sys.argv) != 3:
	usage()
	exit()

#opening both input files and naming output file
bbhfile=open(sys.argv[1], "rU")
fastafile=open(sys.argv[2], "rU")
outname=sys.argv[1].split(".blast")[0]+".fasta"
#reading input files into program and closing inputfile
bbh=bbhfile.readlines()
fasta_all=fastafile.read()
bbhfile.close()
fastafile.close()
#splitting the fasta into a list of each sequence
fasta=fasta_all.split(">")

#making output file
output=open(outname, "w")
#going through each line in the bbh file/list
for line in bbh:
	name=line.split("\t")[0]
#	going through each sequence in the fasta file/list
	for seq in fasta:
		seqname=seq.split("\n")[0]
#		if the fasta sequence name matches the best hit name, write that fasta seq to file
		if name == seqname:
			output.write(">"+seq)
output.close()