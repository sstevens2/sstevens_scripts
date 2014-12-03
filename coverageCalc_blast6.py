#!/usr/bin/python

import sys, csv, os

"""coverageCalc_blast6.py: Calculates coverage of each subject from blast outfmt 6 results"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: coverageCalc_blast6.py <blastResults>"
	sys.exit(2)

if len(sys.argv) != 2:
	usage()
	exit()

inputfile=sys.argv[1]
sortedfile=inputfile+".sort"

os.system("sort -k2 -t $'\t' "+inputfile+" > "+sortedfile)

seplist=[]
#reading in file and writing each contigs hits to separate list within seplist
with open(sortedfile,'rb') as tsvin:
	tsvin = csv.reader(tsvin, delimiter='\t')
	index=0
	templist=[]
	lastsubject=''
	for row in tsvin:
		if index==0:
			templist.append(row)
			lastsubject=row[1]
#			print "1st if"
		elif lastsubject == row[1]:
			templist.append(row)
#			print "2nd if"
		else:
			seplist.append(templist)
			templist=[row]
#			print "else"
		lastsubject=row[1]
		index+=1
	seplist.append(templist)
#print seplist
#print len(seplist)

#set up outfile
outfile=inputfile+".cov.tsv"
output=open(outfile, "w")

all_covcount=[]
for contig in seplist:
	covcount=[]
	for hit in contig:
		end = int(hit[9])
		start= int(hit[8])
		if int(hit[8]) > int(hit[9]):
			end = int(hit[8])
			start= int(hit[9])
#		print hit
		if int(end) >= (len(covcount)):
#			print len(covcount)
			diff= (end)-len(covcount)+1
#			print diff
			covcount=covcount+[0]*diff
#			print len(covcount)
		for base in range(start,end+1):
			covcount[base]=covcount[base]+1
#	all_covcount.append(covcount)
	output.write(contig[0][1]+"\t")
	for base in covcount:
		output.write(str(base)+"\t")
	output.write("\n")
output.close()