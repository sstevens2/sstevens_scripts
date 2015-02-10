#!/usr/bin/env python

#Sarah Stevens
#sstevens2@wisc.edu

import sys, Bio, re
from Bio import SeqIO
from Bio.Data import CodonTable

def usage():
	print("Usage: find_nvsn_sites.py [genbank_file] [codonsyninfo.txt]")
	print("This program counts the number of synonymous and nonsynonymous sites for each gene in a genbank file. Requires the file with the information about codon syn and non syn sites.")

if len(sys.argv) != 3:
	usage()
	exit()

#reading all the inputs and setting up outputs
inputfile = open(sys.argv[1], "rU")
inputfile2 = open(sys.argv[2], "rU")
codoninfo = inputfile2.readlines()
codoninfolist = []
for line in codoninfo:
	codoninfolist.append(line.split("\n")[0].split("\t"))
codoninfolist.pop(0)
recordlist = []
for record in SeqIO.parse(inputfile, "genbank"):
	recordlist.append(record)
inputfile.close()
handle = sys.argv[1].split(".")[0]+".tsv"
outputfile = open(handle,"w")
outputfile.write("contig_info\tlocus_tag\t")
outputfile.write("AAA	AAC	AAG	AAT	ACA	ACC	ACG	ACT	AGA	AGA	AGG	AGT	ATA	ATC	ATG	ATT	CAA	CAC	CAG	CAT	CCA	CCC	CCG	CCT	CGA	CGC	CGC	CGT	CTA	CTC	CTC	CTG	GAA	GAC	GAG	GAT	GCA	GCC	GCG	GCT	GGA	GGC	GGG	GGT	GTA	GTC	GTG	GTT	TAA	TAC	TAG	TAT	TCA	TCC	TCG	TCT	TGA	TGC	TGG	TGT	TTA	TTC	TTG	TTT\tsyn_sites\tnonsyn_sites\n")


#taking each contig's CDS features and counting the # of each codon within, then printing that number and the total nonsyn and syn calculated after using the given codonsyninfo
allcontigslist = []
for contig in recordlist:
	allgeneslist = []
	for feature in contig.features:
		if feature.type == "CDS":
			seq=feature.extract(contig.seq)
			checkcodons=[seq[i:i+3] for i in range(0,len(seq), 3)]
			tempcodoncount = [['AAA', 0], ['AAC', 0], ['AAG', 0], ['AAT', 0], ['ACA', 0], ['ACC', 0], ['ACG', 0], ['ACT', 0], ['AGA', 0], ['AGA', 0], ['AGG', 0], ['AGT', 0], ['ATA', 0], ['ATC', 0], ['ATG', 0], ['ATT', 0], ['CAA', 0], ['CAC', 0], ['CAG', 0], ['CAT', 0], ['CCA', 0], ['CCC', 0], ['CCG', 0], ['CCT', 0], ['CGA', 0], ['CGC', 0], ['CGC', 0], ['CGT', 0], ['CTA', 0], ['CTC', 0], ['CTC', 0], ['CTG', 0], ['GAA', 0], ['GAC', 0], ['GAG', 0], ['GAT', 0], ['GCA', 0], ['GCC', 0], ['GCG', 0], ['GCT', 0], ['GGA', 0], ['GGC', 0], ['GGG', 0], ['GGT', 0], ['GTA', 0], ['GTC', 0], ['GTG', 0], ['GTT', 0], ['TAA', 0], ['TAC', 0], ['TAG', 0], ['TAT', 0], ['TCA', 0], ['TCC', 0], ['TCG', 0], ['TCT', 0], ['TGA', 0], ['TGC', 0], ['TGG', 0], ['TGT', 0], ['TTA', 0], ['TTC', 0], ['TTG', 0], ['TTT', 0]]
			for countingcodon in tempcodoncount:
				for checkcodon in checkcodons:
					match = re.match(countingcodon[0],str(checkcodon))
					if match != None:
						countingcodon[1] = countingcodon[1]+1
			outputfile.write(contig.description+"\t"+str(feature.qualifiers['locus_tag'][0])+"\t")
			totalsyn = 0
			totalnonsyn = 0
			for codon in tempcodoncount:
				index = tempcodoncount.index(codon)
				outputfile.write(str(codon[1])+"\t")
				totalsyn = totalsyn + (float(codon[1])*float(codoninfolist[index][1]))
				totalnonsyn = totalnonsyn + (float(codon[1])*float(codoninfolist[index][2]))
			outputfile.write(str(totalsyn)+"\t"+str(totalnonsyn)+"\t\n")
			allgeneslist.append([feature, tempcodoncount])
	allcontigslist.append([contig, allgeneslist])


outputfile.close()
		

