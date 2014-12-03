#!/usr/common/usg/languages/python/2.7.4/bin/python

#for genepool...edited there....

import sys, os

def usage():
	print "Usage: cp_refset.py listofRefs  savetolocation"

if len(sys.argv) !=3:
	usage()
	exit()
	
reffile=open(sys.argv[1], "rU")
reflist=reffile.readlines()
reffile.close()
path2save=sys.argv[2]

for line in reflist:
	os.system("cp /global/projectb/projectdirs/microbial/img_web_data/taxon.fna/"+line.split("\t")[0]+".fna "+path2save)