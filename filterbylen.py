import sys, os, Bio

def usage():
	print "Usage: filterbylen.py pathtofiles minlen"
	print ""

if len(sys.argv) != 3:
	usage()
	exit()

path2files=sys.argv[1]
minlen=int(sys.argv[2])
from Bio import SeqIO

for filename in os.listdir(path2files):
	if filename.split(".")[-1]=="fasta":
		output_name=filename.split(".")[0]
		fastafile=open(filename, "rU")
		records = list(SeqIO.parse(fastafile, "fasta"))
		fastafile.close()
		recordlist=[]
		for record in records:
			if len(record.seq) >= minlen:
				recordlist.append(record)
		output_handle=open(output_name+".fasta","w")
		SeqIO.write(recordlist, output_handle, "fasta")