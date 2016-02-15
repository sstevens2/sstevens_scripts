#!/usr/bin/python

import sys, os

def usage():
	print "Usage: blastFWSAGsVMetas.py pathtoSAGs pathtoMetas"


if len(sys.argv) != 3:
	usage()
	exit()
	
path2SAGs=sys.argv[1]
path2metas=sys.argv[2]

print path2SAGs
print path2metas

for SAGname in os.listdir(path2SAGs):
	os.system("makeblastdb -in "+path2SAGs+SAGname+" -out "+path2SAGs+SAGname+".db -dbtype nucl")
	#print("makeblastdb -in "+path2SAGs+SAGname+" -out "+path2SAGs+SAGname+".db -dbtype nucl")
	SAGdb=path2SAGs+SAGname+".db"
	for metaname in os.listdir(path2metas):
		outmeta=metaname.split(".")[0]
		outSAG=SAGname.split("_")[0]
		os.system("blastn -task blastn -db "+SAGdb+" -query "+path2metas+metaname+" -out "+path2SAGs+outmeta+"-vs-"+outSAG+ ".blast -evalue 0.001 -perc_identity 95")
		#print("blastn -task blastn -db "+SAGdb+" -query "+path2metas+metaname+" -out "+outmeta+"-vs-"+outSAG+ ".blast -evalue 0.001 -perc_identity 90 -outfmt 6 -num_threads 20")

	

