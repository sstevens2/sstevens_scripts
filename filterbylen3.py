#!/usr/bin/python

import sys, os

def usage():
	print "Usage: filterbylen2.py fastafile minlen"
	print "Doesn't use Bio package, only keeps seqs >=minlen"

if len(sys.argv) != 3:
	usage()
	exit()

filename=sys.argv[1]
minlen=int(sys.argv[2])

output_name=os.path.splitext(filename)[0]+".lenfilt+str(minlen)
#output_name=filename.split(".")[0]+".lenfilt"+str(minlen)
print "Working on "+ output_name
fastafile=open(filename, "rU")
fasta=fastafile.read()
fastafile.close()
reads=fasta.split(">")
readslist=[]
for read in reads:
	split=read.split("\n")
	seq="".join(split[1:-1])
	if len(seq) >= minlen:
		#print split[0], len(seq)
		readslist.append([split[0],seq])
outputfile=open(output_name+".fa", "w")
for read in readslist:
	outputfile.write(">"+read[0]+"\n"+read[1]+"\n")
outputfile.close()

