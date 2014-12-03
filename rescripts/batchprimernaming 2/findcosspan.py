#!/usr/bin/env python

#Usage findcosspan.py [pairstatus.txt] [scaffolds.txt]

import sys, os


def usage():
	print "Usage: findcosspan.py [pairstatus.txt] [scaffolds.txt]"

if not len(sys.argv) == 3:
	usage()
	exit(2)

pairstatuslist=[]
filename = "allcosspans.txt"
FILE = open(filename,"w")


newfile = open(str(sys.argv[1]), "r")
pairstatus=newfile.readlines()
newfile2 = open(str(sys.argv[2]), "r")
scaffolds=newfile2.readlines()
for line in pairstatus:
	newline=line.split('\t')
	pairstatuslist.append(newline)
coslist=[]
scaffoldslist=[]
count=1
for line in scaffolds:
	newline=line.split('\t')
	if newline[4] == 'N':
		scaffoldslist.append([count, count+1, newline[1],newline[2]])
		count=count+1

for gap in scaffoldslist:
	FILE.write("gap " + str(gap) + " \n")
	for cosmid in pairstatuslist:
		if cosmid[1] == 'TruePair':
			leftend=int(cosmid[4])
			rightend=int(cosmid[7])
			if int(cosmid[4]) > int(cosmid[7]):
				leftend=int(cosmid[7])
				rightend=int(cosmid[4])
			if (leftend < int(gap[2])) and (rightend > int(gap[3])):
				FILE.write(cosmid[0] + " " + str(leftend) + " "+ str(rightend) + "\n")
				
FILE.close()