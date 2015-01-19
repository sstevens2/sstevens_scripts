#!/usr/bin/python

import sys, os, string, random

def usage():
	print "Usage: SAGgeneseditnames.py fastafile namekey.txt"

if len(sys.argv) !=3:
	usage()
	exit()
	
fasta=open(sys.argv[1], "rU")
listfa =fasta.readlines()
fasta.close()
output=open(sys.argv[1].split(".faa")[0]+"_short.faa", "w")
output2=open(sys.argv[2], "w")

index=0
for line in listfa:
	if line.startswith(">"):
		newline=">"+sys.argv[1].split(".faa")[0]+"_"+str(index)+"\n"
		output.write(newline)
		output2.write(line.split("\n")[0]+"\t"+newline)
		index+=1
	else:
		output.write(line)
output.close()
output2.close()
