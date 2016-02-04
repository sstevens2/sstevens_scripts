#!/usr/local/bin/python3

import sys, os
import pandas as pd

"""compareSAGhits.py: finding out how many reads hit to different SAGs, from blast results"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print("Usage: compareSAGhits.py catblastfile")

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

# Function to intersect two Series of Readnames and return length
def intersectHits(s1, s2):
    """ Intersects two numpy series and returns the number of hits in common"""
    return len(set(s1) & set(s2))

# Read in file as DataFrame
input = pd.read_table(sys.argv[1],delim_whitespace=True, header=None)
# Add a new column that is just the Readname split from the 1st[1] column
input['READ']=input[1].str.split('.blast:').str.get(1)
# Add a new column that is just the SAG name from the 2nd[2] column
input['SAG']=input[2].str.split('_').str.get(0) # need if using value counts later
# Get unique SAG names
refs=input['SAG'].unique()
# Make output DataFrames
hitsout_df=pd.DataFrame(index=refs, columns=refs) # Raw number of hits
percout_df=pd.DataFrame(index=refs, columns=refs) # Percentage of ref's hits
# For each SAG
for ref in refs:
    # Subset the data by that SAG
    ref_df=input[input['SAG'] == ref]
    # For each other SAG
    for ref2 in refs:
        ref2_df=input[input['SAG'] == ref2]
        if ref == ref2: # Sanity check.. the same SAG vs itself should return the number of unique reads for that SAG
            assert intersectHits(ref_df['READ'], ref2_df['READ']) == len(set(ref_df['READ']))
        ref2_df=input[input['SAG'] == ref2]
        hitsout_df.set_value(ref,ref2,intersectHits(ref_df['READ'], ref2_df['READ']))
        #Add percentage version...
        percout_df.set_value(ref,ref2,(intersectHits(ref_df['READ'], ref2_df['READ'])/float(len(set(ref_df['READ'])))))

# Write *out_df's to files
hitsout_df.to_csv(sys.argv[1]+'.compHIT', sep='\t')
percout_df.to_csv(sys.argv[1]+'.compPERC', sep='\t')
