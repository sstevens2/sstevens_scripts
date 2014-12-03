#!/usr/bin/env python

import sys, os

def usage():
	print "Usage: countmetareads.py pathtoMetas outfile"


if len(sys.argv) != 3:
	usage()
	exit()

path2metas=sys.argv[1]
outputfile = open(sys.argv[2], "w")

for file in os.listdir(path2metas):
	print file
	returned=os.system("perl perl-cmdtools/cfasta "+path2metas+file)
	outputfile.write(file.split(".")[0]+"\t"+"perl perl-cmdtools/cfasta "+path2metas+file+"\n")

outputfile.close()