#!/usr/bin/python

import sys, os, glob, pandas as pd

def usage():
    print("Usage: calculateCovVals.py 'blastfiles(glob)' metagenomeSizeFile genomeSizeFile")
    print("This program was designed to put the following data tables together:")
    print("number of hits, average ani, covered bases, genome coverage, and genome coverage normalized by metagenome size")
    print("Requires properly formated data tables - FILL IN DETAILS HERE LATER")

if len(sys.argv) != 4:
    usage()
    exit()

# Inputs
files = glob.glob(sys.argv[1])

## Reading in all the files

dflist=[] # list of all the dataframes read in
for infile in files:
    df = pd.read_table(infile, sep=r"\s*", names=['season', 'read', 'contig', 'PID', 'align_len', 'mismatches', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bit_score'])
    dflist.append(df)
all_df = pd.concat(dflist) #concats all dataframes together
all_df['SAG'] = all_df['contig'].str.split('_').str.get(0) # Adds SAG name to column

### Reading in the metagenome and genome files
metaSize_df = pd.read_table(sys.argv[2], sep = '\t', names = ['metaFile','bp'])
metaSize_df = metaSize_df.groupby('metaFile').sum().reset_index() # puts together pooled timepoints
metaSize_df['season'] = metaSize_df['metaFile'].str.split('.').str.get(0)
genSize_df = pd.read_table(sys.argv[3], sep='\t', names = ['genFile','bp'])
genSize_df['SAG'] = genSize_df['genFile'].str.split('_').str.get(0)

## Analysis

## Group by SAG and season (ss)
ssgroup = all_df.groupby(['SAG','season'])

## Makes hit table
hit_table= ssgroup.count().reset_index()[['SAG','season','read']]
hit_table.columns=['SAG','season','hits']

## Counts covered bases (align_len - gaps)
covbase_table = ssgroup.sum().reset_index()[['SAG','season','align_len','gaps']]
covbase_table['cov_base']=covbase_table['align_len']-covbase_table['gaps']

## Calculates Genome Coverage for each season and SAG
genCov_table = covbase_table.merge(genSize_df, on='SAG',how='left')
genCov_table['genCov'] = genCov_table['cov_base'] / genCov_table['bp']
genCov_table = genCov_table[['SAG','season','genCov']]

## Calculates Genome Coverage for each season and SAG normalized by metagenome size
normCov_table = genCov_table.merge(metaSize_df, on='season', how='left')
normCov_table['normCov'] = normCov_table['genCov'] / normCov_table['bp']
normCov_table = normCov_table[['SAG','season','normCov']]

## Calculates ANI for each season and SAG
pid_table = ssgroup.mean().reset_index()[['SAG','season','PID']]


## Outputing files
### Pivots all tables
hit_out = hit_table.pivot(index='SAG', columns='season', values='hits')
covbase_out = covbase_table.pivot(index='SAG',columns='season',values='cov_base')
genCov_out = genCov_table.pivot(index='SAG',columns='season', values='genCov')
normCov_out = normCov_table.pivot(index='SAG',columns='season',values='normCov')
pid_out = pid_table.pivot(index='SAG', columns='season', values='PID')
### Write output to files
hit_out.to_csv('hit_table.txt', sep = '\t')
covbase_out.to_csv('covered_bases.txt', sep = '\t')
genCov_out.to_csv('genome_cov.txt', sep = '\t')
normCov_out.to_csv('normalized_cov.txt', sep ='\t')
pid_out.to_csv('pid.txt', sep='\t')