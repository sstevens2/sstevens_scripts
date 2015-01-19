#!/usr/bin/env python

import sys, os, csv

"""blastCoverageCalc_2.py takes the blast results from a set of SAGs vs. a set of metagenomes,
	where the blasts were done with the set of SAGs as one inputfile.
	The output should be a file for EACH SAG with the columns for the coverage of each base of the metagenome,
	each row is the coverage of a specific metagenome (HZHZ_vs_contig1) for a specific contig in the SAG.
	"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: blastCoverageCalc_2.py path2blastresults"

if len(sys.argv) != 2:
	usage()
	exit()

#read in the set of blast results in folder
#get the names of all the SAGs
#for each SAG
#create output file for each SAG
#find all hits on that SAG
