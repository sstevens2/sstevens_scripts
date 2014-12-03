#!/usr/bin/env python

codons = "AAA	AAC	AAG	AAT	ACA	ACC	ACG	ACT	AGA	AGA	AGG	AGT	ATA	ATC	ATG	ATT	CAA	CAC	CAG	CAT	CCA	CCC	CCG	CCT	CGA	CGC	CGC	CGT	CTA	CTC	CTC	CTG	GAA	GAC	GAG	GAT	GCA	GCC	GCG	GCT	GGA	GGC	GGG	GGT	GTA	GTC	GTG	GTT	TAA	TAC	TAG	TAT	TCA	TCC	TCG	TCT	TGA	TGC	TGG	TGT	TTA	TTC	TTG	TTT"
codonlist = codons.split("	")
printlist=[]
for codon in codonlist:
	printlist.append([codon, 0])
print printlist