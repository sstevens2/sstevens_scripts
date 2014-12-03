#!/usr/bin/python

import sys, os

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
outputfile=open("combined_taxonomy.txt", "w")
outputfile.write("name\tsuperkingdom\tphylum\tclass\torder\tfamily\tgenus\tspecies\n")
for line in taxlist:
	outputfile.write(line[0]+"\t")
	for taxon in line[1]:
		outputfile.write(taxon.split("\n")[0].split(": ")[1]+"\t")
	outputfile.write("\n")
outputfile.close()
