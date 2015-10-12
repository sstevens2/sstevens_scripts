#!/usr/bin/env python

import sys, os, glob

def usage():
	print "Usage: AAI_calculate.py glob2rbb"
	print "Need the _short.faa files in the same directory"
	print "And naming is generally important"
	print "To be used in conjunction with AAI_BLASTnPARSE.py"


if len(sys.argv) != 2:
	usage()
	exit()

filelist=glob.glob(sys.argv[1])

genomelist=[]
##get a list of all the genome names
for file in filelist:
	if file.endswith(".rbb"):
		if file.split("_")[0] not in genomelist:
			genomelist.append(file.split("_")[0])
##print len(genomelist)

outlist1=[]
outlist2=[]
##create lists of the right size to save the final values to
for item in genomelist:
	fakelist=['empty'] * len(genomelist)
	fakelist2=['empty'] * len(genomelist)
	outlist1.append(fakelist)
	outlist2.append(fakelist2)

##get all the numbers and organize them into lists
for genome in genomelist:
	genomefile=open(genome+"_short.faa", "rU")
	genome_content=genomefile.read()
	genes=genome_content.count('>')
#	print genome, genes
	for file in filelist:
		if file.split("_")[0] == genome:
			pid_total=0
			tmp_file=open(file, "rU")
			lines=tmp_file.readlines()
			for line in lines:
#				print line.split("\t")[2]
#				print float(line.split("\t")[2])
				pid_total=pid_total+float(line.split("\t")[2])
			pid=pid_total/len(lines)
			row=genomelist.index(file.split("_")[0])
			column=genomelist.index(file.split("_")[1].split("v")[-1])
#			print file, row, column, pid
			outlist1[row][column]=pid
			outlist2[row][column]=float(len(lines))/float(genes)
# 			print file, float(len(lines))/float(genes)
			

##write all the list files to output
aniout=open("AAI_out.txt", "w")
genesout=open("Gmatches_out.txt", "w")
aniout.write("\t")
genesout.write("\t")
for genome in genomelist:
	aniout.write(genome+"\t")
	genesout.write(genome+"\t")
aniout.write("\n")
genesout.write("\n")

for row in outlist1:
	aniout.write(genomelist[outlist1.index(row)]+"\t")
	for column in row:
		aniout.write(str(column)+"\t")
	aniout.write("\n")
	
for row in outlist2:
	genesout.write(genomelist[outlist2.index(row)]+"\t")
	for column in row:
		genesout.write(str(column)+"\t")
	genesout.write("\n")

aniout.close()
genesout.close()
		
		
		
				
