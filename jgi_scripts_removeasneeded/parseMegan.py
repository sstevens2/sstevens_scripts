#!/usr/common/usg/languages/python/2.7.4/bin/python

import sys, os

def usage():
	print "Usage: parseMEGAN.py Taxonfasta"

if len(sys.argv) !=2:
	usage()
	exit()
	
fastafile= open(sys.argv[1], "rU")
fasta=fastafile.readlines()
fastafile.close()
name=sys.argv[1].split("/")[-1].split(".fasta")[0]
output=open(name+"_parse.txt", "w")

for line in fasta:
	if line.startswith(">"):
		output.write(line.split(">")[1].split("\n")[0]+"\t"+name+"\n")

output.close()