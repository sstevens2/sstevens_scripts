#!/usr/bin/env python

import sys, os, csv

def usage():
	print "Usage: parseBLASTSAGsvsMetaResults.py path2blastresults"
	print "Blast results should be separated into folders by reference genome"
	print "However, all metagenomes results for the same reference should be together"

if len(sys.argv) != 2:
	usage()
	exit()

path2files=sys.argv[1]

def aPercID(hitfile):
	total=0
	count=0
	for hit in hitfile:
		total=total+float(hit[2])
		count+=1
	return count, total/count


outMetas=[]
outPercID=[]
outnumhits=[]
for file in os.listdir(path2files):
	if file.endswith(".len200"):
		with open(path2files+file,'rb') as tsvin:
			tsvin = csv.reader(tsvin, delimiter='\t')
			hits, avgPID = aPercID(tsvin)
			outMetas.append(file.split(".")[0])
			outPercID.append(avgPID)
			outnumhits.append(hits)

name=os.listdir(path2files)[0].split(".blast")[0].split("-")[-1]
outname=path2files+name+'.percID'
outname2=path2files+name+'.numhits'
with open(outname, 'wt') as out:
	with open(outname2, 'wt') as out2:
		out.write("\t")
		out2.write("\t")
		for meta in outMetas:
			out.write(meta+'\t')
			out2.write(meta+'\t')
		out.write('\n')
		out.write(name+'\t')
		out2.write('\n')
		out2.write(name+'\t')
		for number in outPercID:
			out.write(str(number)+'\t')
			out2.write(str(outnumhits[outPercID.index(number)])+'\t')
		out.write('\n')
		out2.write('\n')