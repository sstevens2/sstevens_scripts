import sys, os

def usage():
	print "Usage: tbnamesfix.py pathtofiles"

#only made this program to rename some files from JGI

if len(sys.argv) != 2:
	usage()
	exit()
	
path2files=sys.argv[1]

for filename in os.listdir(path2files):
	if filename.split(".")[-1]=="fasta":
		id=filename.split(".")[2]
		newfilename = "fail"
		fastafile=open(path2files+"/"+filename, "rU")
		if filename.split(".")[0] == "lake_hypo":
			newfilename="TB_hypo_"+id+".fna"
		if filenmae.split(".")[0] == "lake_epi":
			newfilename="TB_hypo_"+id+".fna"
		outfile=open(newfilename, "w")
		outfile=write(fastafile.read())
		outfile.close()