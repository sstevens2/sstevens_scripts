#!/usr/bin/python

import sys, os, string, random

def usage():
	print "Usage: SAGgeneseditnames.py fastafile"

if len(sys.argv) !=2:
	usage()
	exit()
	
fasta=open(sys.argv[1], "rU")
listfa =fasta.readlines()
fasta.close()
output=open(sys.argv[1].split(".faa")[0]+"_short.faa", "w")
output2=open(os.path.splitext(sys.argv[1])[0]+"_faanamekey.txt", "w")

index=0
for line in listfa:
	if line.startswith(">"):
		reindex="%04d" % index
		newline=">"+sys.argv[1].split(".faa")[0]+"_"+str(reindex)+"\n"
		output.write(newline)
		output2.write(line.split("\n")[0]+"\t"+newline)
		index+=1
	else:
		output.write(line)
output.close()
output2.close()
