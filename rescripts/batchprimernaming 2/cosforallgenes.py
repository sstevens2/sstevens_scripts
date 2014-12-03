#!/usr/bin/env python

# Usage: cosforallgenes.py [genome.gbk] [pairstatus.txt] [vector.gbk]

import sys, os, Bio

def usage():
	print "Usage: cosforallgenes.py [genome.gbk] [pairstatus.txt] [vector.gbk]"
	print "The genbank file can be from either RAST or from genbank."
	print "However one must use the pairstatus file that is output"
	print "from using gsMapper to map the cosmids to the fasta file"
	print "which corresponds to same genbank file used."
	
if not len(sys.argv) == 4:
	usage()
	exit(2)

##Create file to out put all the cosmids which span a feature(gene)
filename = "cosspans4genes.txt"
cosspanfile = open(filename,"w")
cosspanfile.write("This file lists each of the features in the genome and which cosmids span those features.")
cosspanfile.write("\r")
cosspanfile.write("If the cosmid listed has a 'False Pair' status, then it should be verified with PCR to be sure it really spans that region.")
cosspanfile.write("\r")
cosspanfile.write("The cosmid lines list the names of the cosmids as well as other information about start and end sites, though generally all one will need is the name.")
cosspanfile.write("\r")
cosspanfile.write("\r")

#Import the genbank file and read it in
#Also genome_length is defined for later
from Bio import SeqIO
fullgenome = SeqIO.read(sys.argv[1], "genbank")
vector = SeqIO.read(sys.argv[3], "genbank")
genome_length=len(fullgenome.seq)

##Import the Pair file
newfile = open(str(sys.argv[2]), "r")
pairfile=newfile.readlines()
##Get rid of the headers
pairfile.pop(0)
##Make the pairfile into a list of lists for easier browsing
pairstatlist = []
for item in pairfile:
	pairstatlist.append(item.split("\t"))
print "Succesfully imported Pairstatus file"
#print  "How are you?"

##Finds all the Falsepair cosmids which actually
##Span from the end to the beginning and creates a list.
##Then writes a genbank file to reflect it
endspanlist = []
for cosmid in pairstatlist:
	if cosmid[1] == 'FalsePair':
		smallend=int(cosmid[4])
		bigend=int(cosmid[7])
		if smallend > bigend:
			smallend=int(cosmid[7])
			bigend=int(cosmid[4])
		endlength = genome_length - bigend
		beglength = smallend
		if 25000 < (endlength + beglength) < 40000:
			endspanlist.append(cosmid)
			filename2 = str(cosmid[0])+ ".gbk"
			fileinquestion = open(filename2,"w")
			if cosmid[5] == "-":
				cosmidX = vector + (fullgenome[bigend:] + fullgenome[:smallend]).reverse_complement()
			else:
				cosmidX = vector + (fullgenome[bigend:] + fullgenome[:smallend])
			cosmidX.name = cosmid[0]
			cosmidX.id = cosmid[0]
			cosmidX.description = "Extraxted cosmid from " + fullgenome.name + '.  ' + "This is an endspaning cosmid and needs to be verified by PCR."
			SeqIO.write(cosmidX, fileinquestion, "genbank")
			fileinquestion.close()
print "Found " + str(len(endspanlist)) + " cosmids spanning the end"
#print "I think I saw you on the stree the other day"

##For each TP cosmid, make a genbank file to reflect it
##For each cosmid which spans over the end, make a genbank file to reflect it
for cosmid in pairstatlist:
	if cosmid[1] == 'TruePair':
		filename2 = str(cosmid[0])+ ".gbk"
		fileinquestion = open(filename2,"w")
		leftend=int(cosmid[4])
		rightend=int(cosmid[7])
		if leftend > rightend:
			leftend=int(cosmid[7])
			rightend=int(cosmid[4])
		if cosmid[5] == "-":
			cosmidX = vector + fullgenome[leftend:rightend].reverse_complement()
		else:
			cosmidX = vector + fullgenome[leftend:rightend]
		cosmidX.name = cosmid[0]
		cosmidX.id = cosmid[0]
		cosmidX.description = "Extraxted cosmid from " + fullgenome.name
		SeqIO.write(cosmidX, fileinquestion, "genbank")
		fileinquestion.close()
print "Genbank file made for each cosmid"
#print "Why won't you answer me!?!?!?"



##Go through all the features and pull out all the cosmids which span each
##Then write the resultes to a file
for feature in fullgenome.features:
	cosspanfile.write(str(feature))
	cosspanfile.write("\r")
	for cosmid in pairstatlist:
		if cosmid[1] == 'TruePair':
			leftend=int(cosmid[4])
			rightend=int(cosmid[7])
			if leftend > rightend:
				leftend=int(cosmid[7])
				rightend=int(cosmid[4])
			if (leftend < int(feature.location.nofuzzy_start)) and (rightend > int(feature.location.nofuzzy_end)):
				for column in cosmid:
					cosspanfile.write(column + "\t")
				cosspanfile.write("\r")
	for cosmid in endspanlist:
		smallend=int(cosmid[4])
		bigend=int(cosmid[7])
		if smallend > bigend:
			smallend=int(cosmid[7])
			bigend=int(cosmid[4])
		if (bigend < int(feature.location.nofuzzy_start)) and (genome_length > int(feature.location.nofuzzy_end)) or (0 < int(feature.location.nofuzzy_start)) and (smallend > int(feature.location.nofuzzy_end))  :
			for column in cosmid:
				cosspanfile.write(column + "\t")
			cosspanfile.write("\r")
	cosspanfile.write("\r")
print "Found all cosmids spanning each gene"
#print "Oh well.... *leaves*"



os.system("mkdir cosmids_gbk")
os.system("mv SS* cosmids_gbk")

cosspanfile.close()
