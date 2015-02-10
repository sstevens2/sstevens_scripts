#!/usr/bin/python

import sys, csv, os

"""filterGeneLenGeneGainLoss.py is for filtering the results of Metastats and removing the
	genes that don't pass the len filter of 450 bp
	One off script
"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: filterGeneLenGeneGainLoss.py inputfile"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

inputfile=sys.argv[1]
allfile=inputfile.split('.txt')[0]+'.txt'
allin=open(allfile, 'rt')
#allin=open('batch1/'+allfile, 'rt')
alltxt=allin.readlines()
header=alltxt[0]

filtlist=[]
ctslist=[]
with open(inputfile,'rb') as filtin:
	filtin = csv.reader(filtin, delimiter='\t')
	for row in filtin:
		for find in alltxt:
			find=find.split('\t')
			if row[0] == find[1]:
				if int(find[2]) > 450:
					ctslist.append(find)
					filtlist.append(row)

#inputfile=inputfile.split('.0513')[0]+".0709"+inputfile.split('.0513')[1]
output=open(inputfile+".len450",'wt')
output2=open(inputfile+'.len450.counts', 'wt')
output2.write(header)
for line in ctslist:
	index=ctslist.index(line)
	for item in line:
		if not item.endswith('\n'):
			output2.write(item+'\t')
		else:
			output2.write(item)
	for item in filtlist[index]:
		output.write(item+'\t')
	output.write('\n')
output.close()
output2.close()