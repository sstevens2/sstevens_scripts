#!/usr/bin/python

import sys, os, string, random

def usage():
	print "Usage: fakenames16.py fastafile"

if len(sys.argv) !=2:
	usage()
	exit()

fasta=open(sys.argv[1], "rU")
listfa =fasta.readlines()
fasta.close()
output=open(sys.argv[1].split(".")[0]+"_renamed.fna", "w")
namelist=open(sys.argv[1].split(".")[0]+"_namelist.txt", "w")
namesgenerated=[]

def generatename():
	name=''.join(random.choice(string.ascii_uppercase) for i in range(16))
	return name

for line in listfa:
	if line.startswith(">"):
		nname=generatename()
		while nname in namesgenerated:
			nname=generatename()
		namesgenerated.append(nname)
		namelist.write(line.split("\n")[0]+"\t"+nname+"\n")
		output.write(">"+nname+"\n")
	else:
		output.write(line)
output.close()
namelist.close()

