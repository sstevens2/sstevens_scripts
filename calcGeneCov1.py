#!/usr/bin/python

import sys, os, pickle

"""calcGeneCov.py: takes the coverage results from(from coverageCalc_blast6.py) after fixed by
	lenfixsep_coverage.py and calculate the average coverage of each gene in
	each of the metagenomes.  Needs the .cov.split.tsv files in one folder, and one with the 
	info pulled out by gbk_extractGeneInfo2.py
	This is likely a one off script for the acI_SAGs work, depends on naming scheme"""

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
		year=file.split('_')[2]
		month=file.split('_')[3].split('.')[0]
		metalist.append(year+'_'+month)
#print len(metalist)		


def getAvg(contig, start, end):
	sublist=contig[start:end]
	print "contig", contig[0]
	print "contiglen", len(contig)
	print "start", start
	print "end", end
	print "sublen", len(sublist)
	if len(sublist) != (end-start):
		print "AHHH SUBLENTH IS WRONG"
	avg= sum(map(int, sublist))/float(len(sublist))
	return avg

def findContig(meta, contig):
	gi_contig=contig[0]
	tindex=gi_contig.split('_')[-1]
	try:
		test=meta[int(tindex)]
		if gi_contig in test:
			return test
	except IndexError:
		pass
	for line in meta:
		if gi_contig in line:
			return line
	return 'no contig'

for SAG in SAGlist:
	#open the gene_info file
	SAG_gi_file=open(path2SAG_gi+SAG+'_norrna_short.tsv','rU')
	SAG_gi=SAG_gi_file.readlines()
	#make output file
	output=open(SAG+'gene_cov.tsv','w')
	#write metagenomes in order to first row of file
	output.write('locus_tag\t')
	for meta in metalist:
		output.write(meta+'\t')
	output.write('\n')
	print "Working on " + SAG
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
			matched_con=findContig(hitlist, sline)
			if matched_con == 'no contig':
				output.write('N/A\t')
			else:
				print locus_tag, meta
				average=getAvg(matched_con, start, end)
				output.write(str(average)+'\t')
		output.write('\n')
	output.close()
