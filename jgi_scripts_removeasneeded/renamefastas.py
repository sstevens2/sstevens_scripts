#!/usr/common/usg/languages/python/2.7.4/bin/python

#only to rename files from binning for comparison

import sys, os

def usage():
	print "Usage: renamefastas.py inputfile"

if len(sys.argv) !=2:
	usage()
	exit()

file=open(sys.argv[1], "rU")
output=open(sys.argv[1].split("_renamed")[0]+".fa", "w")
output.write(file.read())
output.close()
file.close()
