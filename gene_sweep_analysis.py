#!/usr/bin/python

import sys, os
import pandas as pd

"""gene_sweep_analysis.py: looking for regions where SNPs sweep"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: gene_sweep_analysis.py file_TFfixed.tsv windowsize"
	print "windowsize specifies how many SNPs in a row must sweep in a region, must be an integer and > 1"

if len(sys.argv) != 3:
	usage()
	sys.exit(2)

#input values
input = pd.read_table(sys.argv[1],sep='\t')
reg_value = int(sys.argv[2]) # sets size of region to check for sweep, ex. 3 SNPs in a row
years = ['Y2005', 'Y2007', 'Y2008', 'Y2009', 'Y2012', 'Y2013']

#functions
def check_sweep(input_list, chrom_list, reg): #checks each sliding window to see if there are the right number of trues in a row, provided they are on the same contig
	outlist=[]
	for i, row in enumerate(input_list):
		if i < (len(input_list)-(reg-1)):
			for j in range(0,reg):
				index=i+j
				if chrom_list[i] != chrom_list[index]: #breaks it if the first SNP and any SNP in the window are not in the same contig
					break
				elif input_list[index]==False:
					break
			else:
				outlist.append(i)
	return outlist

def make_indexlist(sweepfilt_dict, reg): #makes list of all the rows which are actually in the gene region that sweeps
	all_sweep=list() #all the lines which sweep
	for item in sweepfilt_dict:
		for i in sweepfilt_dict[item]:
			for j in range(0,reg):
				index=j+i
				if index not in all_sweep:
					all_sweep.append(index)
	return sorted(all_sweep)

def check_byfirstyear(sweep_indict, years_list): # compares each years sweeping regions and removes those which were considered swept in the first year
	sweep_filt=dict() #regions that sweep in each year, excluding those which were already true in 1st year
	for name in years_list[1:]:
		sweeps_set=list(set(sweep_indict[name]) & (set(sweep_indict[name]) ^ set(sweep_indict[years_list[0]])))
		if sweeps_set:
			sweep_filt[name]=sweeps_set
	return sweep_filt

sweep_dict=dict() #regions that sweep in each year
for name in years:
		sweeps_fd=check_sweep(input[name], input['CHROM'], reg_value) # returning the list of regions that sweep
		sweep_dict[name]=sweeps_fd

sweep_filt=check_byfirstyear(sweep_dict, years) #checking that the sweep was not true in the first year
#swept_regions=make_indexlist(sweep_filt, reg_value)

##print sweep_filt
##print swept_regions

#make counts of each year
counts=dict()
for item in sweep_filt:
	counts[item] = len(sweep_filt[item])
#print counts

#writing counts to output
filename=sys.argv[1].split('_')[0]
header='window_size\t'
outline=filename+'_'+str(reg_value)+'\t'
for name in years: # loop to put together header and output line of counts
	header=header+name+'\t'
	if name in counts: #checks if year has any count
		outline=outline+str(counts[name])+'\t'
	elif name == years[0]: # writes na if this is the first year
		outline=outline+'na'+'\t'
	else: #writes 0 if there is were no windows found
		outline=outline+'0'+'\t'

header=header[:-1]+'\n'
outline=outline[:-1]+'\n'
outname=os.path.splitext(sys.argv[1])[0]+"_counts.tsv"
if os.path.isfile(outname):
	with open(outname, "a") as output:
		output.write(outline)
else:
	with open(outname, "w") as output:
		output.write(header+outline)

