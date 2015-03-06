#!/usr/bin/python

import sys, os
import pandas as pd
import numpy as np

"""gene_sweep_analysis.py: looking for regions where SNPs sweep"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: gene_sweep_analysis.py file_TFfixed.tsv intsweepsize"
	print "intsweepsize is an integer which specifies how many SNPs must sweep in a region"

if len(sys.argv) != 3:
	usage()
	sys.exit(2)

input = pd.read_table(sys.argv[1],sep='\t')
reg_value = int(sys.argv[2]) # sets size of region to check for sweep, ex. 3 SNPs in a row
##print input['Y2005']

def check_sweep(input_list, reg): #checks each sliding window to see if there are the right number of trues in a row
	outlist=[]
	for i, row in enumerate(input_list):
		if i < (len(input_list)-(reg-1)):
			for j in range(0,reg):
				index=i+j
				if input_list[index]==False:
					break
			else:
				outlist.append(i)
	return outlist

def make_indexlist(sweepfilt_dict, reg): #makes list of all the rows which are actually in the gene region that sweeps
	all_sweep=list() #all the lines which sweep
	for item in sweepfilt_dict:
##		print item, sweepfilt_dict[item]
		for i in sweepfilt_dict[item]:
			for j in range(0,reg):
				index=j+i
				if index not in all_sweep:
					all_sweep.append(index)
	return sorted(all_sweep)

##check_sweep(input['Y2005'])
years = ['Y2005', 'Y2007', 'Y2008', 'Y2009', 'Y2012', 'Y2013']
sweep_dict=dict() #regions that sweep in each year
for name in years:
	sweeps_fd=check_sweep(input[name], reg_value)
##	print name, sweeps_fd
	sweep_dict[name]=sweeps_fd
##print sweep_dict

sweep_filt=dict() #regions that sweep in each year, excluding those which were already true in 1st year
all_sweep=list() #all the lines which sweep
for name in years[1:]:
	sweeps_set=list(set(sweep_dict[name]) & (set(sweep_dict[name]) ^ set(sweep_dict[years[0]])))
	if sweeps_set:
		sweep_filt[name]=sweeps_set

swept_regions=make_indexlist(sweep_filt, reg_value)
print swept_regions

##print list(set(all_sweep))
##print sweep_filt

counts=[]
for item in sweep_filt:
	print item, len(sweep_filt[item])
