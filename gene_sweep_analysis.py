#!/usr/bin/python

import sys, os, pandas

"""gene_sweep_analysis.py: looking for regions where SNPs sweep"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: gene_sweep_analysis.py <file_TFfixed.tsv>"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)


