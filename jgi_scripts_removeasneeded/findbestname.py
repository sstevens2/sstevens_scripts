#!/usr/common/usg/languages/python/2.7.4/bin/python

import sys, os

def usage():
	print "Usage: findbestname.py filenamelist path2parsed cp2dir"

if len(sys.argv) !=4:
	usage()
	exit()

filenamefile=open(sys.argv[1], "rU")
filenamelist=filenamefile.readlines()
filenamefile.close()
path2parsed=sys.argv[2]
cp2dir=sys.argv[3]
suffixlist=[".prob+1.0.perc1.0.txt", ".prob+1.0.perc0.9.txt", ".prob+1.0.perc0.8.txt", ".prob+0.9.perc1.0.txt", ".prob+0.9.perc0.9.txt", ".prob+0.9.perc0.8.txt", ".prob+0.8.perc1.0.txt", ".prob+0.8.perc0.9.txt", ".prob+0.8.perc0.8.txt"]
	

for file in filenamelist:
	max=0
	for suffix in suffixlist:
		name=path2parsed+file.split("\n")[0]+suffix
		filesize=os.path.getsize(name)
		if max < filesize:
			max = filesize
	#print max
	for suffix in suffixlist:
		name=path2parsed+file.split("\n")[0]+suffix
		filesize=os.path.getsize(name)
		if filesize == max:
			os.system("cp "+name+" "+cp2dir)
			break