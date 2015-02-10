import sys, os

def usage():
	print "Usage: tbnamesfix.py pathtofiles"

#only made this program to rename some files from JGI

if len(sys.argv) != 2:
	usage()
	exit()
	
path2files=sys.argv[1]

for filename in os.listdir(path2files):
	if filename.split(".")[-1]=="fa":
		id=filename.split(".")[2]
		fastafile=open(path2files+"/"+filename, "rU")
		newfilename="ME_"+id+".fna"
		outfile=open(newfilename, "w")
		outfile.write(fastafile.read())
		outfile.close()