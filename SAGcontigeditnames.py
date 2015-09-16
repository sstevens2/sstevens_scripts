#!/usr/bin/python

import sys, os, string, random

"""
This program takes a fna file and renames each entry with the name of the file and a 3 digit number
"""

def usage():
	print "Usage: SAGcontigeditnames.py fastafile"

if len(sys.argv) !=2:
	usage()
	exit()

fasta=open(sys.argv[1], "rU")
listfa =fasta.readlines()
fasta.close()
output=open(os.path.splitext(sys.argv[1])[0]+"_short.fna", "w")
output2=open(os.path.splitext(sys.argv[1])[0]+"_namekey.txt", "w")

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
