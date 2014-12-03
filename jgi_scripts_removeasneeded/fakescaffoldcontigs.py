#!/usr/bin/python python

import sys, os

def usage():
	print "Usage: fakescaffoldcontigs.py fastafile  outputfilename"

if len(sys.argv) !=3:
	usage()
	exit()

fasta=open(sys.argv[1], "rU")
listfa =fasta.readlines()
fasta.close()
output=open(sys.argv[2], "w")
listfa.pop(0)
output.write(">"+ sys.argv[1]+"\n")
for line in listfa:
	if line.startswith(">"):
		output.write("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\n")
	elif line.startswith("\n"):
		x=line
	else:
		output.write(line)
output.close()