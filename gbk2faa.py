#!/usr/bin/env python

import sys, os

def usage():
	print "Usage: gbk2faa.py gbkfile"


if len(sys.argv) != 3:
	usage()
	exit()

gbk = sys.argv[1]

outname=file.split(".gb")[0]
os.system("cat "+path2gbk+file+"| gex2.pl cds > "+path2fna+outname+".faa")