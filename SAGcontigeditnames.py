#!/usr/bin/python

import sys, os, string, random

def usage():
	print "Usage: SAGcontigeditnames.py fastafile"

if len(sys.argv) !=2:
	usage()
	exit()
	
fasta=open(sys.argv[1], "rU")
listfa =fasta.readlines()
fasta.close()
output=open(sys.argv[1].split(".fasta")[0]+"_short.fna", "w")
output2=open(sys.argv[1]+"_namekey.txt", "w")

index=0
for line in listfa:
	if line.startswith(">"):
		reindex="%03d" % index
		newline=">"+sys.argv[1].split("_")[0]+"_"+str(reindex)+"\n"
		output.write(newline)
		output2.write(line.split("\n")[0]+"\t"+newline)
		index+=1
	else:
		output.write(line)
output.close()
output2.close()
