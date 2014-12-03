#!/usr/bin/env python

#Sarah Stevens
#sstevens2@wisc.edu

import sys

def usage():
	print("Usage: orderSNPSandsites.py [SNPsbyloci.tsv] [Sitesbyloci.tsv] [output.tsv]")
	print("This program combines the output of countingSNPsbyloci.py and find_svsns_sites.py so you can look at only the sites for the loci with SNPs.")
	
if len(sys.argv) != 4:
	usage()
	exit()
	
outputfile = open(sys.argv[3], "w")
outputfile.write("SNP_loci\tsite_loci\tsyn_SNPs\tnonsyn_SNPs\tsyn_sites\tnonsyn_sites\n")
snpsfile = open(sys.argv[1], "rU")
sitesfile = open(sys.argv[2], "rU")
snps = snpsfile.read()
snpslist = []
snpsloci = []
snpslines = snps.split("\n")
for item in snpslines:
	snpslist.append(item.split("\t"))
	snpsloci.append(item.split("\t")[0])
sites = sitesfile.read()
siteslist = []
sitesloci = []
siteslines = sites.split("\n")
for item in siteslines:
	siteslist.append(item.split("\t"))
	try:
		sitesloci.append(item.split("\t")[1])
	except IndexError:
		blabla=0
#print snpslist[0]
#print siteslist[0][67]
snpslist.pop(0)
snpsloci.pop(0)
siteslist.pop(0)
sitesloci.pop(0)

combinedlist = []
for item in snpsloci:
	snpsindex = snpsloci.index(item)
	sitesindex = sitesloci.index(item)
	outputfile.write(snpslist[snpsindex][0]+"\t"+siteslist[sitesindex][1]+"\t"+snpslist[snpsindex][1]+"\t"+snpslist[snpsindex][2]+"\t"+siteslist[sitesindex][66]+"\t"+siteslist[sitesindex][67]+"\n")
	
outputfile.close()
	