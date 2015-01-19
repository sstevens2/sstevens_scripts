#!/usr/bin/python

import sys, csv

"""rm_lowcorrcontigs.py  - this program takes out contigs from the fna files
	of GFMs that don't meet the correlation value cutoffs.  Created for
	specific temporary function. """

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: rm_lowcorrcontigs.py corrcutofffile"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

in_name=sys.argv[1]
inputfile=open(sys.argv[1], "rU")
input=inputfile.readlines()
inputfile.close()

corcontigs=[]
for item in input:
	corcontigs.append(item.split("\t")[0].split("_")[-1])

path2files="/global/dna/projectdirs/RD/singlecell/Projects/timeseries/bins/tb_hyp/"
name_prefix="TH"
if in_name.startswith("TE"):
	path2files="/global/dna/projectdirs/RD/singlecell/Projects/timeseries/bins/tb_epi/"
	name_prefix="TE"

fasta_name= in_name.split('.tsv')[0]+".fa"

fastafile=open(path2files+fasta_name, "rU")
fasta= fastafile.read()
fastafile.close()
fasta_s=fasta.split(">")
fasta_s.pop(0)
output=open(fasta_name, "w")

x=0
for contig in fasta_s:
	if contig.split("\n")[0].split("_")[-1] in corcontigs:
		output.write(">"+contig)
output.close()


"""
#old format, reformating to my version
filenum=in_name.split(firstsplit)[1].split("_")[0].lstrip("0")
filenum2=in_name.split(firstsplit)[1].split(".")[0].lstrip("0")
fasta_name=name_prefix+".metabat."+filenum+".fa"

fastafile=open(path2files+fasta_name, "rU")
fasta= fastafile.read()
fastafile.close()

fasta_s=fasta.split(">")
fasta_s.pop(0)
output=open(name_prefix+".metabat."+filenum2+".cor.fa", "w")
x=0
for contig in fasta_s:
	if contig.split("\n")[0].split("_")[-1] in corcontigs:
		output.write(">"+contig)
output.close()
"""