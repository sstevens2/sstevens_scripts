#!/usr/bin/python

import sys, csv

"""rm_lowcorrcontigs.py  - this program takes out contigs from the fna files
	of GFMs that don't meet the correlation value cutoffs.  Created for
	specific temporary function. """

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: rm_lowcorrcontigs.py corrcutofffile"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

in_name=sys.argv[1]
inputfile=open(sys.argv[1], "rU")
input=inputfile.readlines()

path2files="/home/sstevens2/Metabat_bins_transferred05222014/TBhypo"
name_prefix="TBhypo"
if in_name.startswith("TE"):
	path2files="/home/sstevens2/Metabat_bins_transferred05222014/TBepi"
	name_prefix="TBepi"

filenum=in_name.split("0")[1].split(".")[0]
fasta_name=nameprefix+".metabat."+filenum+".fa"
print fasta_name