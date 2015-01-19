#!/usr/bin/python

import sys, os

def usage():
	print "Usage: blastSAGVMetas.py SAGfasta pathtoMetas"
	print "Makes db and runs blastn with the following settings"
	print "-evalue 0.001 -perc_identity 95 -outfmt 6"
	


if len(sys.argv) != 3:
	usage()
	exit()
	
SAGname=sys.argv[1]
path2metas=sys.argv[2]


os.system("makeblastdb -in "+SAGname+" -out "+SAGname+".db -dbtype nucl")
#print("makeblastdb -in "+SAGname+" -out "+SAGname+".db -dbtype nucl")
SAGdb=SAGname+".db"
for metaname in os.listdir(path2metas):
	if metaname.endswith(".fasta"):
		outmeta=metaname.split(".fasta")[0]
		outSAG=SAGname.split(".fasta")[0]
#		print("blastn -task blastn -db "+SAGdb+" -query "+path2metas+metaname+" -out "+outmeta+"-vs-"+outSAG+ ".blast -evalue 0.001 -perc_identity 95 -outfmt 6")
		os.system("blastn -task blastn -db "+SAGdb+" -query "+path2metas+metaname+" -out "+outmeta+"-vs-"+outSAG+ ".blast -evalue 0.001 -perc_identity 95 -outfmt 6")