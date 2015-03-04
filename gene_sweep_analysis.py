#!/usr/bin/python

import sys, os
import pandas as pd
import numpy as np

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
sweep_dict=dict() #regions that sweep in each year
for name in years:
	sweeps_fd=check_sweep(input[name])
##	print name, sweeps_fd
	sweep_dict[name]=sweeps_fd
##print sweep_dict

sweep_filt=dict() #regions that sweep in each year, excluding those which were already true in 1st year
all_sweep=list() #all the lines which sweep
for name in years[1:]:
	sweeps_set=list(set(sweep_dict[name]) & (set(sweep_dict[name]) ^ set(sweep_dict[years[0]])))
	if sweeps_set:
		sweep_filt[name]=sweeps_set
		for item in sweeps_set:
			if item not in all_sweep:
				all_sweep.append(item)
			if (item+1) not in all_sweep:
				all_sweep.append(item)
			if (item+2) not in all_sweep:
				all_sweep.append(item)
print set(all_sweep)
print sweep_filt