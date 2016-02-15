#!/usr/bin/python

import sys, os, glob, subprocess
from multiprocessing import Pool

def usage():
	print "Usage: blastSAGVMetas.py 'path2SAGsfasta(glob)' 'metagenomes(glob)' threads(int)"
	print "Makes db and runs blastn with the following settings"
	print "-evalue 0.001 -outfmt 6 -perc_identity 95"

if len(sys.argv) != 4:
	usage()
	exit()
	
path2SAGs=sys.argv[1]
path2Metas=sys.argv[2]
threads=int(sys.argv[3])

def call_blast(params):
	SAGname, metaname = params
	SAGdb=SAGname+".db"
	outSAG=os.path.basename(os.path.splitext(SAGname)[0])
	outmeta=os.path.basename(os.path.splitext(metaname)[0])
	outname=outmeta+'-vs-'+outSAG+'.blast'
	cmd=['blastn', '-task blastn', '-db '+SAGdb, '-query '+metaname,'-out '+outname, '-evalue 0.001', '-outfmt 6','-perc_identity 95']
	print ' '.join(cmd), os.getpid() #testing line, left in for log file
	os.system(' '.join(cmd)) #replace with subprocess when you figure it out
	#subprocess.call(cmd)

if __name__ == '__main__':
	p=Pool(threads)
	#print path2SAGs
	SAGfiles=glob.glob(path2SAGs)
	metafiles=glob.glob(path2Metas)
	#print SAGfiles
	#all possible combos of SAGs vs Metagenomes
	inlist=[]
	for SAG in SAGfiles:
		os.system('makeblastdb -in '+SAG+' -out '+SAG+'.db'+' -dbtype nucl')
		for meta in metafiles:
			inlist.append([SAG, meta])
	#print inlist
	p.map(call_blast,inlist)
	p.close()

