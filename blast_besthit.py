#!/usr/local/bin/python3

import sys, os
import pandas as pd

"""blast_besthit.py: pulling out only the best hit from blast results (in outfmt 6)"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

#print this if not right number of inputs
def usage():
	print("Usage: blast_besthit.py blastfile")
	print("blast file needs to be in outfmt 6")

#check if right number of inputs
if len(sys.argv) != 2:
	usage()
	exit()



"""
#opening input file, just saves location in memory
blastinput=sys.argv[1]
blastfile=open(blastinput, "rU")
#reading each line of the input file into a list of rows
blast=blastfile.readlines()
#closes save location, because already read row into file
blastfile.close()

#for each row, split into columns and save
blastlist=[]
for line in blast:
	blastlist.append(line.split("\t"))

#for each row, save name if not saved before
uniques=[]
for row in blastlist:
	if row[0] not in uniques:
		uniques.append(row[0])

#breaks up the list by unique names
splitblast=[]
for unique in uniques:
	templist=[]
	for row in blastlist:
		if unique == row[0]:
			templist.append(row)
	splitblast.append(templist)

#for each chunk, finds best hit and saves to list
finallist=[]
for item in splitblast:
	max=0.0
	item2save=[]
	for row in item:
		value=float(row[2])
		if value > max:
			max=value
			item2save=row
	finallist.append(item2save)

#writes all best hits to file
outputname=blastinput.split(".")[0]+"_bbh.blast"
output=open(outputname, "w")
for item in finallist:
	for col in item:
		if not col.endswith("\n"):
			output.write(col+"\t")
		else:
			output.write(col)
output.close()
"""