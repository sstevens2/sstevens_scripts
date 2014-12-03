#!/usr/bin/env python

import sys, os, Bio, re

def usage():
	print "Usage: batchalignandtree.py [checkarg]"
	print "This program is meant to be run with clusters2fasta.py."
	print "It needs to be in a filefolder with all the fasta files for each cluster."
	print "Must have only fasta files in the diretory to work"
	print "Add a random string in the check argument area to run."


if len(sys.argv) != 2:
	usage()
	exit()

#go to every file in the current working directory and run t_coffee for it
for filename in os.listdir(os.getcwd()):
	os.system("t_coffee " + filename + " -mode=mcoffee -output=phylip -n_core=1")
#Move all the output files to folders corresponding to filetype
os.mkdir("dnd")
os.mkdir("phylip")
os.system("mv *.dnd dnd/")
os.system("mv *.phylip phylip/")
#Remove the crapfile that always seems to come out of this
os.system("rm wrong.file")

#Switch to the directory containing the phylip alignments
os.chdir("phylip")

#Go through every file in the phylip directory, make a directory for that cluster's tree files, 
#move the alignment to that directory, switch into that directory, searches for the best aa model, 
#then it runs raxml for the file with the best aa model, then go back up one directory (to the phylip directory)
index=1
for filename in os.listdir(os.getcwd()):
	if str(filename).startswith("cluster"):
		os.mkdir("treeset"+str(index))
		os.system("cp "+ filename + " treeset"+str(index))
		os.chdir("treeset"+str(index))
		directory=os.getcwd()
		os.chdir("/Users/mcmahon15inch2010/Documents/Sarah/programs/prottest-3.2-20130314")
		os.system("java -jar prottest-3.2.jar -i "+ directory+"/"+filename+ " -AIC -BIC -o "+ directory+"/"+filename+".prottest -Dayhoff -DCMut -JTT -MtREV -WAG -RtREV -CpREV -VT -Blosum62 -MtMam")
		os.chdir(directory)
		os.system("python /Users/mcmahon15inch2010/Documents/Sarah/scripts/parseProttest.py " +filename+".prottest")
		modelfile = open("Prottestsubmodel.txt", "rU")
		model = modelfile.readlines()[0]
		os.system("raxml -f a -x 123456 -p 123456 -#100 -m PROTCAT"+ model+" -s " + filename + " -n " + filename +".raxml -T 2")
		os.chdir("..")
		index=index+1