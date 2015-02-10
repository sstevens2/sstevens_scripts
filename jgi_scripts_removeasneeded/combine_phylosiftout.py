#!/usr/common/usg/languages/python/2.7.4/bin/python

import sys, os

"""combine_phylosift.py: takes a directory with many files from parse_phylosift_sts.py and 
	makes a tab-delimited file with the taxonomy of each listed"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: combine_phylosiftout.py  directoryofparsedSTSs"

if len(sys.argv) !=2:
	usage()
	exit()

path2files=sys.argv[1]
taxlist=[]

for filename in os.listdir(path2files):
	if filename.split(".")[-1]=="txt":
		taxfile=open(path2files+filename, "rU")
		tax=taxfile.readlines()
		taxlist.append([filename, tax])
		taxfile.close()
outputfile=open(path2files+"combined_taxonomy.txt", "w")
outputfile.write("name\tsuperkingdom\tphylum\tclass\torder\tfamily\tgenus\tspecies\n")
for line in taxlist:
	outputfile.write(line[0]+"\t")
	for taxon in line[1]:
		outputfile.write(taxon.split("\n")[0].split(": ")[1]+"\t")
	outputfile.write("\n")
outputfile.close()
