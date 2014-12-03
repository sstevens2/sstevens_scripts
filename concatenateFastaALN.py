#!/usr/bin/python

import sys, os

def usage():
	print "Usage: concatenateFastaALN.py listoffasta2concatenate"


if len(sys.argv) !=2:
	usage()
	exit()

dirfile=open(sys.argv[1], 'rU')
dirlist=dirfile.readlines()
index=0
index2=0
dirlist.pop(0)

for file in dirlist:
	print file
	"""
		if index == 0:
			os.system("t_coffee -other_pg seq_reformat -in "+path2cat+file+" -in2 "+path2cat+dirlist[1]+" -action +cat_aln > "+path2cat+"alnfile"+str(index2)+".fasta")
			print("t_coffee -other_pg seq_reformat -in "+path2cat+file+" -in2 "+path2cat+dirlist[1]+" -action +cat_aln > "+path2cat+"alnfile"+str(index2)+".fasta")
			index2+=1
		elif index > 1:
			os.system("t_coffee -other_pg seq_reformat -in "+path2cat+"alnfile"+str(index2-1)+".fasta -in2 "+path2cat+file+" -action +cat_aln > "+path2cat+"alnfile"+str(index2)+".fasta")
			print("t_coffee -other_pg seq_reformat -in "+path2cat+"alnfile"+str(index2-1)+".fasta -in2 "+path2cat+file+" -action +cat_aln > "+path2cat+"alnfile"+str(index2)+".fasta")
			index2+=1
		else:
			print str(index)+ " yay2"
		index+=1"""