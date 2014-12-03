#/usr/bin/python

import sys, os, time

def usage():
	print "Usage: run_phylosift.py pathtofiles"

if len(sys.argv) != 2:
	usage()
	exit()
	
path2files=sys.argv[1]
outputfile=open("logfile.txt", "w")

for filename in os.listdir(path2files):
	if filename.split(".")[-1]=="fasta":
		#print("./phylosift all "+path2files+"/"+filename)
		os.system("./phylosift all "+path2files+"/"+filename)
		outputfile.write("Ran phylosift on "+filename+time.strftime("  %m/%d/%Y  %H:%M:%S")+"\n")
outputfile.close()