#!/usr/bin/python

import sys, os

"""hitcounts.py finds all the different subjects in the output blast hit files(format 6)
	 in the list given, then it counts how many hits that subject has and creates an 
	 output file for each subject and makes a line giving the name of the hit file, and the
	 number of hits.  Probably a one off script...given it uses the naming scheme"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: calcGeneCov.py <listofblasthitfiles.txt>"

if len(sys.argv) != 2:
	usage()
	sys.exit(2)

listfile=open(sys.argv[1], 'rU')
namelist=listfile.readlines()

#fix filenames and make filelist
filelist=[]
for name in namelist:
	index=namelist.index(name)
	name=name.split('\n')[0]
	namelist[index]=name
	file=open(name, 'rU')
	file=file.read()
	filelist.append(file)
#print filelist[0]

#get subject names
subjects=[]
for line in filelist[0].split('\n'):
	try:
		subject=line.split('\t')[1]
	except IndexError:
		continue
	subject=subject.split('_')[0]
	if subject not in subjects:
		subjects.append(subject)
#print len(subjects)

for subject in subjects:
	output=open(subject+'.hits.txt', "w")
	for file in filelist:
		index=filelist.index(file)
		name=namelist[index].split('.')[0]
		output.write(name+'\t'+str(file.count(subject))+'\n')
	output.close()
	