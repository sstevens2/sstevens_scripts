#!/usr/bin/env python

#Sarah Stevens
#sstevens2@wisc.edu

import sys

def usage():
	print("Usage: countingSNPsbyloci.py [SNPs_file.csv] [output.tsv]")
	print("This program takes a csv file listing all the SNPs found in coding regions by geneious, and counts how many nonsyn and syn SNPs there are for each loci.  It outputs this as a tsv.")

if len(sys.argv) != 3:
	usage()
	exit()
	
inputfile = open(sys.argv[1], "rU")
outputfile = open(sys.argv[2], "w")
outputfile.write("loci\tsyn\tnonsyn\n")
inputlines = inputfile.readlines()

table = []
for line in inputlines:
	table.append(line.split(","))
table.pop(0)


locitable = []
locitable.append(table[0][21])
locicountingsyn = [0]
locicountingnonsyn = [0]

for snp in table:
	try:
		index = locitable.index(snp[21])
		if snp[25] == 'None':
			value = locicountingsyn[index]
			locicountingsyn[index] = value + 1
		else:
			value = locicountingnonsyn[index]
			locicountingnonsyn[index] = value + 1
	except ValueError:
		locitable.append(snp[21])
		if snp[25] == 'None':
			locicountingsyn.append(1)
			locicountingnonsyn.append(0)
		else:
			locicountingsyn.append(0)
			locicountingnonsyn.append(1)

for item in locitable:
	outputfile.write(str(item)+"\t")
	index = locitable.index(item)
	outputfile.write(str(locicountingsyn[index])+"\t")
	outputfile.write(str(locicountingnonsyn[index])+"\n")


outputfile.close()