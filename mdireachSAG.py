#/usr/bin/python

import sys, os

def usage():
	print "Usage: makedireachSAG.py pathtofiles"

#only made this program to make a folder for each SAG in a folder

if len(sys.argv) != 2:
	usage()
	exit()

path2files=sys.argv[1]

for filename in os.listdir(path2files):
	SAGname=filename.split("_")[0]
	os.system("mkdir "+SAGname)
	os.system("mv "+filename+ " " +SAGname)