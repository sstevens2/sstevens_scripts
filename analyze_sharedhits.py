#!/usr/local/bin/python3

import pandas as pd
import argparse
parser = argparse.ArgumentParser(description='analyze_sharedhits.py: Takes the output from compareSAGhits.py and filters it based on set cutoffs')
import numpy as np

"""analyze_sharedhits.py: Takes the output from compareSAGhits.py and filtering it based on set cutoffs"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

#Parse Arguments
parser.add_argument('--perc_in','-pin' , action="store", dest='perc_in', type=str, required=True, metavar='FILE.compPERC', help='The file ending in .compPERC created from compareSAGhits.py')
parser.add_argument('--hits_in','-hin', action="store", dest='hits_in',type=str, required=True, metavar='FILE.compHIT', help='The file ending in .compHIT created from compareSAGhits.py')
parser.add_argument('--perc_lim','-plim', action="store", dest='perc_lim', type=float, choices=np.arange(0,1.01,0.01), default=.20, metavar='.20', help='The cutoff for percent hits shared. i.e. only pairs that share percentages higher than this cutoff will be considered.  Default: .20')
parser.add_argument('--hit_lim','-hlim', action="store", dest='hit_lim',type=int, default=15000, metavar='15000', help='The cutoff for number of hits shared. i.e. only pairs sharing more hits than this cutoff will be considered. Default: 15k')
args=parser.parse_args()


#IMPORT DATA
perc = pd.read_table(args.perc_in, sep='\t',index_col=0)
hits = pd.read_table(args.hits_in, sep='\t',index_col=0)

# Filtering out hits that were below the cutoffs above
perc_out=perc[hits>args.hit_lim]  # removing the values from the percentage table where the hits are too low
perc_out=perc_out[perc>args.perc_lim] # removing the values from the final perc output table where the percentages are too low
hits_out=hits[hits>args.hit_lim]  # removing the values from the hit table where the hits are too low
hits_out=hits_out[perc>args.perc_lim] # removing the values from the final hits output table where the percentages are too low


perc_out = perc_out.stack().reset_index() # stacking only the hits from the table
hits_out = hits_out.stack().reset_index() 


hits_out.columns = ['genome1', 'genome2','hits'] #fixing header
perc_out.columns = ['genome1', 'genome2','perc'] #fixing header
hits_out = hits_out[hits_out['genome1'] != hits_out['genome2']] #filtering out the hits that were selfVself
perc_out =perc_out[perc_out['genome1'] != perc_out['genome2']] #filtering out the hits that were selfVself


hits_out.to_csv('{0}.{1}_hits.{2}_perc'.format(args.hits_in, str(args.hit_lim),str(int(args.perc_lim*100))), sep = '\t')
perc_out.to_csv('{0}.{1}_hits.{2}_perc'.format(args.perc_in, str(args.hit_lim),str(int(args.perc_lim*100))), sep = '\t')






