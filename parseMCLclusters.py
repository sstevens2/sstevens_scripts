#!/usr/bin/env python

import sys, os, re

def usage():
	print "Usage: parseMCLclusters.py [cluster_file] [genome_name_list] [outputfilname.tsv]"
	print "This program takes the product of MCL and a list of genome names and puts them into an tab separated file with the clusters as rows and genomes as columns.  The genome name file must be each genome name on a separate line."

if len(sys.argv) != 4:
	usage()
	exit()

# open all the input and output files
outputfile = open(sys.argv[3], "w")
namesfile = open(sys.argv[2], "rU")
clusterfile = open(sys.argv[1], "rU")

#read in all the names, reformat, and add to list
names = namesfile.readlines()
nameslist = []
for name in names:
	newname = name.split("\n")
	nameslist.append(newname[0])
outputfirstline = "cluster\t"
for name in nameslist:
	outputfirstline = outputfirstline + name + "\t"
outputfirstline = outputfirstline + "\n"
outputfile.write(outputfirstline)
	
#read in all the clusters and add each one to a list and reorganize so each cluster is its own list
clusters = clusterfile.read()
clusterslist = clusters.split("\n")
allclusterslist = []
for cluster in clusterslist:
	allclusterslist.append(cluster.split("\t"))

	
#Search though each cluster and find if each genome has representative gene in that cluster
finalclusterlist = []
for cluster in allclusterslist:
	newclusterlist = []
	for name in nameslist:
		genelist = []
		for gene in cluster:
			match = re.match(name,gene)
			if match != None:
				genelist.append(gene)
		newclusterlist.append(genelist)
	finalclusterlist.append(newclusterlist)

#put info in order and write to file
for cluster in finalclusterlist:
	clusterstr = ""
	for genelist in cluster:
		geneliststr = ""
		for gene in genelist:
			geneliststr = geneliststr + gene + "  "
		clusterstr = clusterstr + geneliststr + "\t" 
	outputfile.write(str(finalclusterlist.index(cluster)+1) + "\t" + clusterstr + "\n")
outputfile.close()
	
	

