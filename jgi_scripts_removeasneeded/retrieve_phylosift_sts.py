#!/usr/common/usg/languages/python/2.7.4/bin/python

import sys, os

def usage():
	print "Usage: retrieve_phylosift_sts.py PSdirectory  SavetoDirectory"

if len(sys.argv) !=3:
	usage()
	exit()

PSdir=sys.argv[1]
savedir=sys.argv[2]

for filename in os.listdir(PSdir):
	#newname=filename.split(".")[0]
	os.system("cp "+ PSdir+filename+"/sequence_taxa_summary.txt "+savedir+filename+"_sts.txt")