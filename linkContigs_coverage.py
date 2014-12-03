#!/usr/bin/python

import sys, csv, os

"""linkContigs_coverage: Links together bases coverage profiles from different contigs in the same results (from coverageCalc_blast6.py).  
							Also takes the output from the conting_len.py (both sets of files need ot have genomes in same order)"""

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

index=0
outname=covfile.split(".")[0]+".cov.cat.tsv"
output=open(outname,"w")
for entry in lenlist:
	SAG=SAGlist[index]
	COVlist=[]
	name=entry[0][0].split("_")[0]
	for contig in entry:
		match=False
		index3=0
		for scontig in SAG:
			if contig[0] == scontig[0]:
				diff=int(contig[1])-(len(scontig)-3)
#				print "diff", diff
				match=True
				SAGindex=SAG.index(scontig)
#				print SAGlist[index][SAGindex]
#				print "without_end", len(SAGlist[index][SAGindex][:-1])
				SAGlist[index][SAGindex]=SAGlist[index][SAGindex][:-1]+['0']*diff
#				print "after", len(SAGlist[index][SAGindex])
#				print "shouldbe", contig[1]
				COVlist=COVlist+SAGlist[index][SAGindex][2:]
		if match==False:
			COVlist=COVlist+['0']*int(contig[1])
	output.write(name+"\t")
	for item in COVlist:
		output.write(item+"\t")
	output.write("\n")
	index+=1