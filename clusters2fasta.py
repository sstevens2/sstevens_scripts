#!/usr/bin/env python

import sys, os, Bio

def usage():
	print "Usage: clusters2fasta.py [clusterfile] [fastafile]"

if len(sys.argv) != 3:
	usage()
	exit()
	
# opens each file
fastafile = open(sys.argv[2], "rU")
clusterfile = open(sys.argv[1], "rU")

# makes a list of each cluster and a list of all clusterlists
clusters=clusterfile.read().split("\n")
clusterlist=[]
for cluster in clusters:
	clusterlist.append(cluster.split("\t"))

#reads in the fastafile to bio
from Bio import SeqIO
records = list(SeqIO.parse(fastafile, "fasta"))
fastafile.close()

# for each cluster, opens a new file with the name of the index, then for each gene in that cluster
# it finds the fasta record with the same name and appends that record to a list, then writes all those
# seqs to the file and goes onto the next cluster
index=1
for cluster in clusterlist:
	newfile=open("cluster"+str(index), "w")
	seqlist=[]
	for gene in cluster:
		for seq in records:
			if seq.name == gene:
				seqlist.append(seq)
	SeqIO.write(seqlist, newfile, "fasta")
	newfile.close()
	index+=1

# moves the clusters all to a directory called fastaclusters
os.mkdir("fastaclusters")
os.system("mv cluster* fastaclusters/")
