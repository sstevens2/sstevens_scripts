#!/usr/bin/env python

import sys, os

def usage():
	print "Usage: gbk2fna.py pathtogbk pathtofna"


if len(sys.argv) != 3:
	usage()
	exit()

path2gbk = sys.argv[1]
path2fna = sys.argv[2]

for file in os.listdir(path2gbk):
	outname=file.split(".gb")[0]
	os.system("cat "+path2gbk+file+"| convertseq gb fa > "+path2fna+outname+".fna")