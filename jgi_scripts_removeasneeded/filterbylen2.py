import sys, os

def usage():
	print "Usage: filterbylen2.py pathtofiles minlen"
	print "Doesn't use Bio package, only keeps seqs >=minlen"

if len(sys.argv) != 3:
	usage()
	exit()

path2files=sys.argv[1]
minlen=int(sys.argv[2])

for filename in os.listdir(path2files):
	if filename.split(".")[-1]=="fasta":
		output_name=filename.split(".")[0]+".len"+str(minlen)
		print "Working on "+ output_name
		fastafile=open(path2files+"/"+filename, "rU")
		fasta=fastafile.read()
		fastafile.close()
		reads=fasta.split(">")
		readslist=[]
		for read in reads:
			split=read.split("\n")
			seq="".join(split[1:-1])
			if len(seq) >= minlen:
				#print len(seq)
				readslist.append([split[0],seq])
			else:
				print len(seq)
		outputfile=open(output_name+".fasta", "w")
		for read in readslist:
			outputfile.write(">"+read[0]+"\n"+read[1]+"\n")
		outputfile.close()