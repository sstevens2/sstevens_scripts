#!/usr/bin/python

import sys, os

"""norm_gene_cov_work.py: takes out the datapoints which are more than 3 stdvs from the mean
	for each timepoint, using the nomalized data"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: norm_gene_cov_work.py <SAG_norm.tsv>"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

# coding: utf-8

## Import statements

# In[1]:

import numpy, scipy, os, sys, pandas


## Opening files and reading into pandas

# In[46]:

inputfile=sys.argv[1]
file=open(inputfile, 'rU')
guts=pandas.read_csv(file, sep='\t')
guts


## Getting the list of all the months(columns) and then going through each column and calculating the stdv

# In[47]:

months=list(guts.columns.values)
months.pop(0)
months.pop(-1)
months

#guts[months[0]].std()

names=[]
stdvs=[]
means=[]
for month in months:
    data=guts[month]
    stdv=data.std()
    mean=data.mean()
    names.append(month)
    stdvs.append(stdv)
    means.append(mean)
   #print month, stdv
print len(stdvs)
print names
print stdvs
print means


## Set up output

# In[50]:

outname=inputfile.split('.')[0]
output=open(outname+'_outnote.txt', 'w') #outnote for outliers notated
output2=open(outname+'_outremv.txt', 'w') #outremv for outliers removed
output.write('locus_tag\t')
output2.write('locus_tag\t')
for season in names:
    output.write(season+'\t')
    output2.write(season+'\t')
output.write('count\tperc\t\n')
output2.write('count\tperc\t\n')


## Want to go through each row

# In[51]:

for row in guts.iterrows():
    locus_tag=row[1][0]
    output.write(locus_tag+'\t')
    output2.write(locus_tag+'\t')
    count=0
#    print row[1][1]
    for col in range(0, len(stdvs)+1):
            if col >= 1:
                cov=row[1][col]
                stdv=stdvs[col-1]
                mean=means[col-1]
#                print locus_tag, cov, stdv, mean
                if (mean-(3*stdv))<cov<(mean+(3*stdv)):
                    output.write(str(cov)+'\t')
                    output2.write(str(cov)+'\t')
                else:
                    output.write('OUT3STDV\t')
                    output2.write('nan\t')
                    count+=1
    perc=count/float(len(names))
    output.write(str(count)+'\t'+str(perc)+'\t'+'\n')
    output2.write(str(count)+'\t'+str(perc)+'\t'+'\n')


# In[ ]:



