#!/usr/bin/python

import sys, csv, os, pickle

"""lenfixsep_coverage: takes the coverage results from(from coverageCalc_blast6.py)  
	and output from the conting_len.py and makes the contigs the right length
	(both sets of files need to have genomes in same order)"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: linkContigs_coverage.py <coverage_results> <len_results>"

if len(sys.argv) != 3:
	usage()
	sys.exit(2)

covfile=sys.argv[1]
lenfile=sys.argv[2]

SAGlist=[]
with open(covfile,'rb') as covin:
	covin = csv.reader(covin, delimiter='\t')
	lastSAG=''
	templist=[]
	index=0
	for row in covin:
		rowname=row[0].split("_")[0]
		if index==0:
			lastSAG=rowname
			templist.append(row)
		elif lastSAG==rowname:
			templist.append(row)
		else:
			SAGlist.append(templist)
			templist=[row]
		lastSAG=rowname
		index+=1
	SAGlist.append(templist)


lenlist=[]
with open(lenfile, 'rb') as lenin:
	lenin = csv.reader(lenin, delimiter='\t')
	lastSAG=''
	templist=[]
	index=0
	for row in lenin:
		rowname=row[0].split("_")[0]
		if index==0:
			lastSAG=rowname
			templist.append(row)
		elif lastSAG==rowname:
			templist.append(row)
		else:
			lenlist.append(templist)
			templist=[row]
		lastSAG=rowname
		index+=1
	lenlist.append(templist)
#print lenlist


index=0 
final_list=[]
for entry in lenlist:
	#pulls out coverage for the SAG corresponding to the lenlist entry
	SAG=SAGlist[index]
	COVlist=[]
	#finds the SAG name
	name=entry[0][0].split("_")[0]
	for contig in entry:
		match=False
		for scontig in SAG:
			if contig[0] == scontig[0]:
				diff=int(contig[1])-(len(scontig)-2)
#				print "diff", diff
				match=True
				SAGindex=SAG.index(scontig)
#				print SAGlist[index][SAGindex]
#				print "without_end", len(SAGlist[index][SAGindex][:-1])
				SAGlist[index][SAGindex]=SAGlist[index][SAGindex][:-1]+['0']*diff
#				print "after", len(SAGlist[index][SAGindex])-1
#				print "shouldbe", contig[1]
				COVlist=COVlist+SAGlist[index][SAGindex][2:]
		if match==False:
			print "Contig"+contig[0]+"has no coverage"
	index+=1
for SAG in SAGlist:
	name=SAG[0][0].split("_")[0]
	outfile=open(name+"_vs_"+covfile.split('.')[0]+'.cov.split.tsv', 'w')
	pickle.dump(SAG, outfile)

#works! see http://stackoverflow.com/questions/899103/python-write-a-list-to-a-file to get out of pickle