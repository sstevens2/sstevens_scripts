#!/usr/local/bin/python3

import sys, os
import pandas as pd

"""compareSAGhits.py: finding out how many reads hit to different SAGs, from blast results"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print("Usage: comparePooledSAGhits.py catblastfile")
	print("finds out how many reads both of a pair SAGs, from blast results")
	print("catblastfile: file with all the blast results from the different genomes to compare")
	print("If you want to see detailed info (which SAG hit it better, difference, etc.), must input best blast hit filter results (bbh)")
	print("You can use blast_besthit(pooled!).py to get this new file")

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

# Functions:

# Function to intersect two Series of Readnames and return length
def intersectHits(s1, s2):
	""" Intersects two numpy series and returns the number of hits in common"""
	return (set(s1) & set(s2))

# Function to parse the whole df into many dfs, one per SAG (or a different col, if needed) and add to dictionary by the sagname
def parseInput(comb_df,parseCol):
	""" Separates out all of the different SAGs into separate df and (saves them in a dictionary) """
	out_dict = dict()
	refs=comb_df['SAG'].unique() # all possible SAGs
	for ref in refs:
		ref_df=comb_df[comb_df[parseCol] == ref]
		out_dict[ref]=ref_df
	return out_dict

# Main:

# Read in file as DataFrame
infile = pd.read_table(sys.argv[1],delim_whitespace=True, header=None,names=['pool','meta_info','ref_info','PID','align_len','mismatches','gaps','q_start','q_end','s_start','s_end','evalue','bit_score'])
# Add a new column that is just the Readname split from the 1st[1] column
infile['READ']=infile['meta_info'].str.split('.blast:').str.get(1)
# Add a new column that is just the SAG name from the 2nd[2] column
infile['SAG']=infile['ref_info'].str.split('_').str.get(0) # need if using value counts later

# dictionary to store all of the SAGs and their df (so we aren't subsetting many times)
infile_parsed = parseInput(comb_df=infile, parseCol='SAG')

# Make output DataFrames
names=list(infile_parsed.keys())
hitsout_df=pd.DataFrame(index=names, columns=names) # Raw number of hits
percout_df=pd.DataFrame(index=names, columns=names) # Percentage of ref's hits

# For each SAG
for ref, ref_df in infile_parsed.items():
	# For each other SAG
	for ref2, ref2_df in infile_parsed.items():
		ref2_df=infile[infile['SAG'] == ref2]
		matchingReads = intersectHits(ref_df['READ'], ref2_df['READ'])
		if ref == ref2: # Sanity check.. the same SAG vs itself should return the number of unique reads for that SAG
			assert len(matchingReads) == len(set(ref_df['READ']))
		# Adding number of hits to output df
		hitsout_df.set_value(ref,ref2,len(matchingReads))
		#Add percentage version...
		percout_df.set_value(ref,ref2,(len(matchingReads)/float(len(set(ref_df['READ'])))))
		# Who hit it best analysis
		## subset the two refs down to only the shared hits
		ref1match = ref_df[ref_df['READ'].isin(matchingReads)]
		ref2match = ref2_df[ref2_df['READ'].isin(matchingReads)]
		#assert len(ref1match) == len(ref2match)
		#assert len(ref_df_bbh) == len(set(ref_df['READ']))
		## sanity check - two refs df are same size
		## Count the hits where ID is equal
		## Count the hits where ID ref1>ref2
		## Count the hits where ID ref2<ref2
		## record difference between ref1-ref2

# Write *out_df's to files
hitsout_df.to_csv(sys.argv[1]+'.compHIT', sep='\t')
percout_df.to_csv(sys.argv[1]+'.compPERC', sep='\t')
