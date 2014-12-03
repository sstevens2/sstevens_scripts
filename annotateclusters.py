#!/usr/bin/python

import sys, os, re, string

def usage():
	print "Usage: annotateclusters.py [cluster_file] [tab_file]"

#This program replaces the locus tags for clusters with the annotation

if len(sys.argv) != 3:
	usage()
	exit()

clusterfile=open(sys.argv[1], "rU")
tsvfile=open(sys.argv[2], "rU")

#print clusterfile.read().split("\n")
#print tsvfile.read().split("\n")[0]

clusters= clusterfile.read()

tsv=[]
#print tsvfile.readlines()
for line in tsvfile.readlines():
	nline= line.split("\t")
	clusters=string.replace(clusters, nline[1], nline[2])
	
#print tsv[0]
#print tsv[1][1]
tsvfile.close()
output=open(sys.argv[1]+".anno.tsv","w")
output.write(clusters)
output.close()


"""
clusters=[]
for line in clusterfile.read().split("\n"):
	clusters.append(line.split("\t"))
print clusters[0]
print clusters[1]

tsv=[]
for line in tsvfile.read().split("\n"):
	tsv.append(line.split("\t"))
#print tsv[0]
print tsv[1]
tsvfile.close()


output=open(sys.argv[1]+".anno.tsv","w")
for object in clusters[0]:
	output.write(object+"\t")
output.write("\n")
for cluster in clusters:
	output.write(cluster[0]+"\t")
	for locus in cluster:
		for line in tsv:
			match = re.match(line[1], locus)
			if match != None:
				print line[2]
				output.write(line[2])
		output.write("\t")
	output.write("\n")
clusterfile.close()
output.close()
"""