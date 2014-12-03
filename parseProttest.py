#!/usr/bin/env python

import sys

def usage():
	print "Usage: parseProttest.py [Prottestoupt-logfile]"

if len(sys.argv) != 2:
	usage()
	exit()

outputfile = open("Prottestsubmodel.txt", "w")
fastafile = open(sys.argv[1], "rU")

for line in fastafile.readlines():
	if line.startswith("Best model according to AIC"):
		outputfile.write(line.split(" ")[5].split("\n")[0].upper())

fastafile.close()
outputfile.close()