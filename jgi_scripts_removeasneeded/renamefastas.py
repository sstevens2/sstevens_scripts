#!/usr/bin/python

#only to rename files from binning
#copied to server, and changed slightly and customized for TB binning

import sys, os

def usage():
	print "Usage: renamefastas.py inputfile"

if len(sys.argv) !=2:
	usage()
	exit()

file=open(sys.argv[1], "rU")
output=open("ME.metabat."+sys.argv[1].split("specific")[-1], "w")
output.write(file.read())
output.close()
file.close()