#!/usr/common/usg/languages/python/2.7.4/bin/python

import sys, os

def usage():
	print "Usage: cp_filteredGFM.py listofFiltered savetolocation path2files nameprefix"

if len(sys.argv) !=5:
	usage()
	exit()
	
reffile=open(sys.argv[1], "rU")
reflist=reffile.readlines()
reffile.close()
path2save=sys.argv[2]
path2files=sys.argv[3]
nameprefix=sys.argv[4]

for line in reflist:
	newname=nameprefix+line.split("veryspecific")[-1]
	os.system("cp "+path2files+line.split("\n")[0]+" "+path2save+newname)
