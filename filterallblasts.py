#!/usr/bin/python

import sys, os

def usage():
	print "Usage: filterallblasts.py pathtofiles"

#only made this program to filter all blast results from blastallmetas.py

if len(sys.argv) != 2:
	usage()
	exit()
	
path2files=sys.argv[1]

for filename in os.listdir(path2files):
	if filename.split(".")[-1]=="blast":
		print("filtersearchio5 -format 8 < "+path2files+filename+" > "+path2files+filename+".outfmt8")