#!/usr/bin/python

import sys, os

def usage():
	print "Usage: concatGFMbyPhylum.py namedfile"
	print "DON'T REUSE, very phenageled(sp?)"

if len(sys.argv) !=2:
	usage()
	exit()

file=open(sys.argv[1], "rU")

list= file.readlines()
phylumlist=[]

for line in list:
#	print line.split("\t")[2].split("\n")[0]
	if line.split("\t")[2].split("\n")[0] not in phylumlist:
		phylumlist.append(line.split("\t")[2].split("\n")[0])
phylumlist.pop(0)
print phylumlist

outlist=[]
for phylum in phylumlist:
	templist=[]
	for line in list:
		if phylum == line.split("\t")[2].split("\n")[0]:
#			templist.append(line.split("\t")[2].split("\n")[0])
			templist.append(line.split("\t")[0].split("_")[0]+"_"+line.split("\t")[0].split("_")[1])
	outlist.append(templist)
#print outlist

index=0
for phylum in outlist:
	printline=""
	for genome in phylum:
		printline=printline+genome+".scaf.fa "
	os.system("cat " + printline + "> " + phylumlist[index]+"_TBhypoGFM170.fa")
	index+=1
