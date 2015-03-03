#!/usr/bin/python

import sys, os
import pandas as pd

"""gene_sweep_analysis.py: looking for regions where SNPs sweep"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: gene_sweep_analysis.py <file_TFfixed.tsv>"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

input = pd.read_table(sys.argv[1],sep='\t')
##print input['Y2005']

def check_sweep(input_list):
	outlist=[]
	for i, row in enumerate(input_list):
		if i < (len(input_list)-2):
			if row == True:
				if input_list[i+1]==True:
					if input_list[i+2] == True:
						outlist.append(i)
	return outlist

##check_sweep(input['Y2005'])
years = ['Y2005', 'Y2007', 'Y2008', 'Y2009', 'Y2012', 'Y2013']
for name in years:
	print name
	sweeps_fd=check_sweep(input[name])
	print sweeps_fd
			