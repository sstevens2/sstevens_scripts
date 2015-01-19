#!/usr/bin/python

import sys, os, csv

"""BLASTcombinestatlists.py combines the results from parseBLASTSAGsvsMETAResults.py which
	pulls out the percentID and percentmappedreads
"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"


def usage():
	print "Usage: BLASTcombinestatlists.py pathtostatlists"



if len(sys.argv) != 2:
	usage()
	exit()

path2stats=sys.argv[1]

namelist=[]
filelist=[]
percID=[]
mapdperc=[]
index=0
for file in os.listdir(path2stats):
	if file.endswith(".statlist"):
		filelist.append(file.split(".")[0])
		with open(file,'rb') as covin:
			covin = csv.reader(covin, delimiter='\t')
			if index == 0:
				for row in covin:
					namelist.append(row[0])
					percID.append([])
					mapdperc.append([])
					percID[namelist.index(row[0])].append(row[1])
					mapdperc[namelist.index(row[0])].append(row[2])
			for row in covin:
				percID[namelist.index(row[0])].append(row[1])
				mapdperc[namelist.index(row[0])].append(row[2])
		index+=1
#print namelist
#print percID
#print mapdperc
#print filelist

ID_out=open("percID.tsv","w")
map_out=open("reasMapped.tsv", "w")
ID_out.write("\t")
map_out.write("\t")
for item in filelist:
	ID_out.write(item +"\t")
	map_out.write(item+"\t")
ID_out.write("\n")
map_out.write("\n")

for item in range(0,len(percID)):
	ID_out.write(namelist[item]+"\t")
	map_out.write(namelist[item]+"\t")
	for var in range(0, len(percID[0])):
		ID_out.write(percID[item][var]+"\t")
		map_out.write(mapdperc[item][var]+"\t")
	ID_out.write("\n")
	map_out.write("\n")

ID_out.close()
map_out.close()
