#!/usr/bin/python

import sys, os, pandas as pd, argparse

"""compareSAGhits.py: finding out how many reads hit to different SAGs, from blast results"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

# Functions:

def parseArgs():
	parser = argparse.ArgumentParser(description='compareSAGhits.py: finding out how many reads hit to different SAGs, from blast results, has extended output for bbh files')
	parser.add_argument('--blast_in','-bin' , action="store", dest='blast_in', type=str, required=True, metavar='catblastoutfm6', help="This should be the concatenated blast file of the different SAGs. Extended functionality if the file is bbh's for each SAG.")
	parser.add_argument('--pooled','-p', action="store_true", dest='pool', default=False, help='If you are using a pooled file, add this flag')
	parser.add_argument('--num_threads', action="store", dest='num_threads',type=int, default=1, metavar='num', help='Number of threads to use if multiprocessing')
	args=parser.parse_args()
	return args.blast_in , args.pool, args.num_threads

# Function to intersect two Series of Readnames and return shared set
def intersectHits(s1, s2):
	""" Intersects two numpy series and returns the number of hits in common"""
	return (set(s1) & set(s2))

# Function to parse the whole df into many dfs, one per SAG (or a different col, if needed) and add to dictionary by the sagname
def parseInput(comb_df,parseCol):
	""" Separates out all of the different SAGs into separate df and (saves them in a dictionary) """
	out_dict = dict()
	bbhbool = True
	refs=comb_df['SAG'].unique() # all possible SAGs
	for ref in refs:
		ref_df=comb_df[comb_df[parseCol] == ref]
		out_dict[ref]=ref_df
		if len(ref_df['read'].unique()) != len(ref_df['read']):
			bbhbool = False
	return out_dict, bbhbool

# Main function to compare hits between two SAGs
def compareHits(refs):
	ref, ref2 = refs
	ref_df = infile_parsed[ref] 
	ref2_df= infile_parsed[ref2]
	matchingReads = intersectHits(ref_df['read'], ref2_df['read'])
	if ref == ref2: # Sanity check.. the same SAG vs itself should return the number of unique reads for that SAG
		assert len(matchingReads) == len(set(ref_df['read']))
	# Adding number of hits to output df
	hitsout_df.set_value(ref,ref2,len(matchingReads))
	#Add percentage version...
	perc = (len(matchingReads)/float(len(set(ref_df['read']))))
	percout_df.set_value(ref,ref2,perc)
	# Who hit it best analysis
	if isBBH:
		## subset the two refs down to only the shared hits
		ref1match = ref_df[ref_df['read'].isin(matchingReads)]#.sort_values('read')
		ref2match = ref2_df[ref2_df['read'].isin(matchingReads)]#.sort_values('read')
		assert len(ref1match) == len(ref2match) #just a sanity check
		#assert (ref1match['read'] == ref2match['read']).all() # are the reads the same and in the same order, not sure this matters with join...
		merged_df = pd.merge(ref1match, ref2match, on='read', how='inner')
		## Count the hits where ID is equal
		equal = (merged_df['bit_score_x'] - merged_df['bit_score_y'] == 0).sum() # number of hits which have equal bit score
		## Count the hits where ID ref1>ref2
		ref1greater = (merged_df['bit_score_x'] - merged_df['bit_score_y'] > 0) # hits which bitscore ref1>ref2 - bool, use .sum() if you want the total
		ref1greater_df = merged_df[ref1greater] #dataframe which has only the hits where bitscore ref1>ref2
		assert len(ref1greater_df) == ref1greater.sum() # sanity check - same size
		ref1greaterDiffPID = (ref1greater_df['PID_x']-ref1greater_df['PID_y']) # difference in PID for all of the hits where bitscore ref1>ref2
		ref1greaterDiffBS = (ref1greater_df['bit_score_x']-ref1greater_df['bit_score_y']) # difference in bitscore for all the hits where bitscore ref1>ref2
		## Count the hits where ID ref2<ref2
		ref1less = (merged_df['bit_score_x'] - merged_df['bit_score_y'] < 0) # hits which bitscore ref1<ref2 - bool, use .sum() if you want the total
		ref1less_df = merged_df[ref1less]
		assert len(ref1less_df) == ref1less.sum() # sanity check - same size
		ref1lessDiffPID = (ref1less_df['PID_x']-ref1less_df['PID_y'])
		ref1lessDiffBS = (ref1less_df['bit_score_x']-ref1less_df['bit_score_y'])
		assert len(matchingReads) == equal + ref1greater.sum() + ref1less.sum() # sanity check - the parts equal, greater and less should add up to total
		## Write line to output (pseduoHeader below)
		# ref1  ref2  num_hits  perc_hits  same  ref1>2  ref1<2  ref1>2_PID_max  ref1>2_PID_mean  ref1>2_PID_min ref1>2_BS_max ref1>2_BS_mean ref1>2_BS_min ref1<2_PID_max ref1<2_PID_mean ref1<2_PID_min ref1<2_BS_max ref1<2_BS_mean ref1<2_BS_min
		sep='\t'
		bbh_out.write(sep.join((ref, ref2, str(len(matchingReads)), str(perc), str(equal), str(ref1greater.sum()), str(ref1less.sum()), str(ref1greaterDiffPID.max()), str(ref1greaterDiffPID.mean()), str(ref1greaterDiffPID.min()), str(ref1greaterDiffBS.max()), str(ref1greaterDiffBS.mean()), str(ref1greaterDiffBS.min()), str(ref1lessDiffPID.max()), str(ref1lessDiffPID.mean()), str(ref1lessDiffPID.min()), str(ref1lessDiffBS.max()), str(ref1greaterDiffBS.mean()), str(ref1lessDiffBS.min()),'\n')))

# Main:
if __name__ == '__main__':
	filename, pooled, num_thr = parseArgs()
	# Read in file as DataFrame
	if pooled:
		infile = pd.read_table(filename,delim_whitespace=True, header=None, index_col=False, names=['pool','meta_info','ref_info','PID','align_len','mismatches','gaps','q_start','q_end','s_start','s_end','evalue','bit_score'])
		# Add a new column that is just the Readname split from the 1st[1] column
		infile['read']=infile['meta_info'].str.split('.blast:').str.get(1)
	else:
		infile = pd.read_table(filename,delim_whitespace=True, header=None, index_col=False, names=['read','ref_info','PID','align_len','mismatches','gaps','q_start','q_end','s_start','s_end','evalue','bit_score'])
	# Add a new column that is just the SAG name from the 2nd[2] column
	infile['SAG']=infile['ref_info'].str.split('_').str.get(0) # need if using value counts later
	# dictionary to store all of the SAGs and their df (so we aren't subsetting many times)
	infile_parsed, isBBH = parseInput(comb_df=infile, parseCol='SAG')
	# Make output DataFrames
	names=list(infile_parsed.keys())
	hitsout_df=pd.DataFrame(index=names, columns=names) # Raw number of hits
	percout_df=pd.DataFrame(index=names, columns=names) # Percentage of ref's hits
	if isBBH:
		print('Your file is a bbh, running extra analysis')
		bbh_out = open(filename+'.compALL', 'w')
		bbh_out.write('ref1\tref2\tnum_hits\tperc_hits\tsame\tref1>2\tref1<2\tref1>2_PID_max\tref1>2_PID_mean\tref1>2_PID_min\tref1>2_BS_max\tref1>2_BS_mean\tref1>2_BS_min\tref1<2_PID_max\tref1<2_PID_mean\tref1<2_PID_min\tref1<2_BS_max\tref1<2_BS_mean\tref1<2_BS_min\n')
	else:
		print('Your file is not a bbh, you will only get the .compHIT and .compPERC files')
	allCombos = list() # list that holds all possible combinations of sag v. sags
	# For each SAG
	for ref in names:
		# For each other SAG
		for ref2 in names:
			allCombos.append([ref,ref2])
	map(compareHits, allCombos)
	# Write *out_df's to files
	hitsout_df.to_csv(filename+'.compHIT', sep='\t')
	percout_df.to_csv(filename+'.compPERC', sep='\t')
	if isBBH:
		bbh_out.close()
