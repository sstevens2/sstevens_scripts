#!/usr/bin/python python

import sys, os, string

def usage():
	print "Usage: fixfakenames.py trefile  outputfilename namelist"

if len(sys.argv) !=4:
	usage()
	exit()

treefile=open(sys.argv[1], "rU")
tre=treefile.read()
treefile.close()
output=open(sys.argv[2], "w")
namelist=open(sys.argv[3], "rU")
names=namelist.readlines()
namelist.close()

for line in names:
	sep=line.split("\t")
	tre=string.replace(tre, sep[1].split("\n")[0],sep[-1].split(">")[1])
output.write(tre)
output.close()
