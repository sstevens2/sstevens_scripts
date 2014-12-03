#!/usr/bin/python

import sys, os, string

def usage():
	print "Usage: matchingTOIDs.py group  MDMrefs outputname"

if len(sys.argv) !=4:
	usage()
	exit()

groupfile = open(sys.argv[1], "rU")
MDMreffile= open(sys.argv[2], "rU")
group=groupfile.readlines()
MDMref=MDMreffile.read()
groupfile.close()
MDMreffile.close()
output=open(sys.argv[3], "w")

#print group[1].split("\t")[0]
#print MDMref

for line in group:
	#print line.split("\t")[0], string.find(MDMref, line.split("\t")[0])
	if string.find(MDMref, line.split("\t")[0]) != -1:
		output.write(line)
output.close()