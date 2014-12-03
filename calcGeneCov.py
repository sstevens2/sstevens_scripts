#!/usr/bin/python

import sys, os, pickle

"""calcGeneCov.py: takes the coverage results from(from coverageCalc_blast6.py) after fixed by
	lenfixsep_coverage.py and calculate the average coverage of each gene in
	each of the metagenomes.  Needs the .cov.split.tsv files in one folder, and one with the 
	info pulled out by gbk_extractGeneInfo2.py
	This is likely a one off script for the acI_SAGs work"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: calcGeneCov.py <coverage_results_dir> <gene_tsv_folder>"

if len(sys.argv) != 3:
	usage()
	sys.exit(2)

#get the list of all of the SAGs from the names of the gene info files
path2SAG_gi=sys.argv[2]
SAGfilelist=os.listdir(path2SAG_gi)
SAGlist=[]
for file in SAGfilelist:
	SAGlist.append(file.split('_')[0])
#print SAGlist

#get a list of all of the metagenomes one set of results of the cov.splits.tsv files
path2covSplits=sys.argv[1]
metafilelist=os.listdir(path2covSplits)
metalist=[]
for file in metafilelist:
	if file.startswith(SAGlist[0]):
		metalist.append(file.split('_')[-1].split('.')[0])
#print len(metalist)

outputlist=[]
for SAG in SAGlist:
	#open the gene_info file
	SAG_gi_file=open(path2SAG_gi+SAG+'_short.tsv','rU')
	SAG_gi=SAG_gi_file.readlines()
	SAG_gi.pop(0)
	SAGout=[]
	locuslist=['\t']
	for meta in metalist:
		#open the metagenome hit file for that SAG for that metagenome
		hitfile=open(path2covSplits+SAG+'_vs_'+meta+'.cov.split.tsv','rU')
		#load in the list file
		hitlist=pickle.load(hitfile)
		#find right contig in hit list
		last_hit=len(hitlist)-1
		templist=[]
		templist.append(meta)
		for line in SAG_gi:
			sline=line.split('\t')
			#write the locus tag to the first col in row of output
			locus_tag=sline[1]
			start=int(sline[2])+1
			end=int(sline[3])+1
			contig=sline[0]
			if locus_tag not in locuslist:
				locuslist.append(locus_tag)
			for c_results in hitlist:
				if contig in c_results:
#					print contig, c_results[0]
					#pull out the part of the list corresponding to the base in the gene
					sublist=c_results[start:end]
					#find the average of coverage for that region
#					print sum(map(int, sublist))/float(len(sublist))
					avg= sum(map(int, sublist))/float(len(sublist))
					templist.append(avg)
					break
				#if that contig is not in the hit file
				elif hitlist.index(c_results)==last_hit:
					templist.append('N/A')
		SAGout.append(templist)
	SAGout.append(locuslist)
	outputlist.append(SAGout)
print outputlist


for SAG in SAGlist:
	index=SAGlist.index(SAG)
	output=open(SAG+'gene_cov.tsv','w')

			
		
		

"""
for SAG in SAGlist:
	#open the gene_info file
	SAG_gi_file=open(path2SAG_gi+SAG+'_short.tsv','rU')
	SAG_gi=SAG_gi_file.readlines()
	#make output file
	output=open(SAG+'gene_cov.tsv','w')
	#write metagenomes in order to first row of file
	output.write('locus_tag\t')
	for meta in metalist:
		output.write(meta+'\t')
	output.write('\n')
	SAG_gi.pop(0)
	for line in SAG_gi:
		sline=line.split('\t')
		#write the locus tag to the first col in row of output
		locus_tag=sline[1]
		output.write(locus_tag+'\t')
		start=int(sline[2])+1
		end=int(sline[3])+1
		contig=sline[0]
		for meta in metalist:
			#open the metagenome hit file for that SAG for that metagenome
			hitfile=open(path2covSplits+SAG+'_vs_'+meta+'.cov.split.tsv','rU')
			#load in the list file
			hitlist=pickle.load(hitfile)
			#find right contig in hit list
			last_hit=len(hitlist)-1
			for c_results in hitlist:
				if contig in c_results:
#					print contig, c_results[0]
					#pull out the part of the list corresponding to the base in the gene
					sublist=c_results[start:end]
					#find the average of coverage for that region
#					print sum(map(int, sublist))/float(len(sublist))
					avg= sum(map(int, sublist))/float(len(sublist))
					#write that number to that col of the file
					output.write(str(avg)+'\t')
					break
				#if that contig is not in the hit file
				elif hitlist.index(c_results)==last_hit:
					output.write('N/A\t')
		output.write('\n')
"""