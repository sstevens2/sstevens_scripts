#!/usr/bin/env python

import sys, os

def usage():
	print "Usage: parseALLvALLblastapart.py inputfile"
	print "Need to update names list for running this with different SAGs and number of SAGs"
	print "DONT USE THIS!  IT USE THE NEWER BETTER SET THAT RUNS ONE AT A TIME"
	
if len(sys.argv) != 2:
	usage()
	exit()

nameslist=['AAA023D18', 'AAA023J06', 'AAA024D14', 'AAA027J17', 'AAA027L06', 'AAA027M14', 'AAA028A23', 'AAA028I14', 'AAA041L13', 'AAA044D11', 'AAA044N04', 'AAA278I18', 'AAA278O22', 'AB141P03']
inputfile=open(sys.argv[1], "rU")
input=inputfile.readlines()

s_list=[]
for name in nameslist:
	matching = [s for s in input if name+"_0" in s.split("\t")[0]][0]
	s_list.append(int(input.index(matching)))
s_list.sort()
#print s_list

finallist=[]
listcheck=0
for item in s_list:
	if s_list.index(item) != 13:
#		print s_list[s_list.index(item)], s_list[s_list.index(item)+1]
		templist=input[s_list[s_list.index(item)]:s_list[s_list.index(item)+1]]
		listcheck+=len(templist)
	else:
		templist=input[s_list[s_list.index(item)]:len(input)]
		listcheck+=len(templist)
	finallist.append(templist)
#print finallist[-1]

for list in finallist:
	name=list[0].split("_")[0]
	outname1=name+"_AAIblastresults.blast"
	outputfile=open(outname1,"w")
	for line in list:
		outputfile.write(line)
	outputfile.close()
#	print("sort -k2 -t $'\t' "+outname1+" > "+outname1+".sorted")



#for item in finallist:
#	print item[0]
#print finallist[1][0]
#print finallist[13][0]

"""
finallist=[]
listtotalcheck=0
for item in s_list:
	templist=input[item[0]:item[1]]
	finallist.append(templist)
	listtotalcheck+=len(templist)
"""
#print listcheck
#print len(input)
#print finallist[13]

"""
for name in nameslist:
	outname1=name+"_AAIblastresults.blast"
	outputfile=open(outname1,"w")
	for line in input:
		if line.split("\t")[0].split("_")[0]==name:
			outputfile.write(line)
	outputfile.close()
	os.system("sort -k2 -t $'\t' "+outname1+" > "+outname1+".sorted")
	inputfile2=open(outname1+".sorted", "rU")
	input2=inputfile2.readlines()
	for name2 in namelist:
		outname2=name+"v"+name2+".sorted"
		outputfile2=open(outname2,"w")
		for line
		
"""