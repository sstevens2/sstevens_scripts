#!/usr/bin/env python

import sys, os

""" parseBLASTSAGsvsMetaResults.py: This program is meant to pull out the number of hits in the metagenome, and write to a file for each SAG
	likely a one off script, unless altered"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"


def usage():
	print "Usage: parseBLASTSAGsvsMetaResults.py inputfile"
	print "Need to update names list for running this with different SAGs"

if len(sys.argv) != 2:
	usage()
	exit()

inputfile=open(sys.argv[1], "rU")
input=inputfile.readlines()
#print input[0:2]

nameslist=['AAA023D18', 'AAA023J06', 'AAA024D14', 'AAA027J17', 'AAA027L06', 'AAA027M14', 'AAA028A23', 'AAA028I14', 'AAA041L13', 'AAA044D11', 'AAA044N04', 'AAA278I18', 'AAA278O22', 'AB141P03']

meta=sys.argv[1].split('.')[0]

all_list=[]
for name in nameslist:
	templist=[]
	for line in input:
		if line.split("\t")[1].split("_")[0] == name:
			templist.append(line)
	file=open(name+".hits.txt", 'at')
	file.write(meta+'\t'+str(len(templist))+'\n')
#	print name, len(templist)
	all_list.append(templist)


"""
leninput=len(input)
outputstats=open(sys.argv[1].split(".blast")[0]+".statlist", "w")
for list in all_list:
	templist=[]
	index=all_list.index(list)
	#outname=sys.argv[1].split(".blast")[0]+"."+nameslist[index]+".blast"
	#outputfile=open(outname, "w")
	countitems=0
	percentIDtotal=0
	for line in list:
		#outputfile.write(line)
		percentIDtotal=percentIDtotal+float(line.split("\t")[2])
	average_percentID=percentIDtotal/len(list)
	percenthits=float(len(list))/float(leninput)
	outputstats.write(nameslist[index]+"\t"+str(average_percentID)+"\t"+str(percenthits)+"\n")
	#outputfile.close()
	
outputstats.close()
"""