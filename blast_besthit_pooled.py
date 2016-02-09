#!/usr/local/bin/python3

import sys, os
import pandas as pd

"""blast_besthit_pooled.py: pulling out only the best hit from pooled blast results (in outfmt 6)"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

#print this if not right number of inputs
def usage():
	print("Usage: blast_besthit.py blastfile")
	print("blast file needs to be in outfmt 6")

#check if right number of inputs
if len(sys.argv) != 2:
	usage()
	exit()

# Read in input
inblast = pd.read_table(sys.argv[1],delim_whitespace=True, header=None,names=['pool','read_info','subject','PID','align_len','mismatches','gaps','q_start','q_end','s_start','s_end','evalue','bit_score'])
inblast['read']=inblast['read_info'].str.split('.blast:').str.get(1)

# Remove duplicates
bs_maxes = inblast.groupby('read').bit_score.transform(max) # finds maxes
bbh_df = inblast[inblast.bit_score == bs_maxes] # keeps only the max values
bbh_df = bbh_df.drop_duplicates('read',keep='first') # removes any duplicates (if both are max)
print('Started with {} hits, kept {} hits'.format(str(len(inblast)), str(len(bbh_df)))) # prints info about number of hits before and after
# Checking that there are no duplicate reads left
checkingdups = bbh_df[bbh_df.duplicated('read') == True] # creates a new dataframe with the repeated rows
assert len(checkingdups) == 0 #shouldn't have any duplicates left and pass this

# Output to file
bbh_df.to_csv(sys.argv[1]+'.bbh', sep='\t', header=False, index=False)
