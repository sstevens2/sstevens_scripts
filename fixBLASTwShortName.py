#!/usr/bin/python python

import sys, os, string

def usage():
	print "Usage: fixBLASTwShortName.py file2change outputfilename namekeylist"

if len(sys.argv) !=4:
	usage()
	exit()

blastfile=open(sys.argv[1], "rU")
blast=blastfile.readlines()
blastfile.close()
output=open(sys.argv[2], "w")
namelist=open(sys.argv[3], "rU")
names=namelist.readlines()
namelist.close()

#print blast[-1]
for line in names:
	for result in blast:
		name=line.split("\t")[1].split(">")[1].split("\n")[0]
		newname=line.split("\t")[0]
		blresult = result.split("\t")[1]
#		print name, blresult
		if name == blresult:
#			print "MATCH"
			newresult=result.replace(blresult, newname)
			output.write(newresult)
output.close()