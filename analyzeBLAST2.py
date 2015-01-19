#!/usr/bin/python

import sys, os

def usage():
	print "Usage: analyzeBLAST.py pathtoBLASTresults SAGID"


if len(sys.argv) != 3:
	usage()
	exit()

path2blastr=sys.argv[1]
outfile=open(sys.argv[2]+"_blastresults.txt", "w")

"""
for blast in os.listdir(path2blastr):
	if blast.split(".")[-1] == "blast":
		os.system("cat "+blast+" | filtercol2 -more -col 4 -value 200 > "+blast.split(".")[0]+".len200")
	
for len200 in os.listdir(path2blastr):
	if len200.split(".")[-1] == "len200":
		os.system("cat "+len200+" | filtercol2 -more -col 3 -value 95 > "+len200.split(".")[0]+".len200.id95")
"""	
outfile.write("Name\t"+sys.argv[2]+"\n")
for id95 in os.listdir(path2blastr):
	if id95.split(".")[-1] == "unique":
		file=open(id95,"rU")
		outfile.write(id95.split("-")[0]+"\t"+str(len(file.readlines()))+"\n")
		
outfile.close()