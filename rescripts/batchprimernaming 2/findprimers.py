#!/usr/bin/env python

#Usage 

import sys, os, csv

def usgae():
	print "Usage: findprimers.py"

if not len(sys.argv) == 1:
	usage()
	exit(2)

fwdprimerlistinfo = [ ]
revprimerlistinfo = [ ]
fwdprimerlist = [ ]
revprimerlist =[ ]

for filename in os.listdir(os.getcwd()):
    if str(filename).endswith('.for'):
    	cosmid = ""
    	gapstart = ""
    	fwdprimerlistinfo.append(str(filename))
    	for item in fwdprimerlistinfo:
    		infosplit = str(item).split(".")
    		cosmid = infosplit[0]
    		scaffold = infosplit[1]
    		gapstart = infosplit[2]
    	newfile = open(filename, "r")
    	primerfile=newfile.readlines()
    	if not len(primerfile)==3:
    		primerseq = primerfile[3].split(' ')
    		#print primerseq
    		fwdprimerlist.append([cosmid,scaffold,gapstart,primerseq[4]])
    	else:
    		fwdprimerlist.append([cosmid,scaffold,gapstart,"no fwd primer"])
#print fwdprimerlist

for filename in os.listdir(os.getcwd()):
    if str(filename).endswith('.rev'):
    	cosmid = ""
    	gapstart = ""
    	revprimerlistinfo.append(str(filename))
    	for item in revprimerlistinfo:
    		infosplit = str(item).split(".")
    		cosmid = infosplit[0]
    		scaffold = infosplit[1]
    		gapstart = infosplit[2]
    	newfile = open(filename, "r")
    	primerfile=newfile.readlines()
    	if not len(primerfile)==3:
    		primerseq = primerfile[3].split(' ')
    		revprimerlist.append([cosmid,scaffold,gapstart,primerseq[4]])
    	else:
    		revprimerlist.append([cosmid,scaffold,gapstart,"no rev primer"])

filename = "primertablefwd.tsv"
FILE = open(filename,"w")
for item in fwdprimerlist:
	FILE.write(str(item[0]) + "\t" + str(item[1]) + "\t" + str(item[2]) + "\t" + str(item[3]) + "\n")
FILE.close()

filename2 = "primertablerev.tsv"
FILE = open(filename2, "w")
for item in revprimerlist:
	FILE.write(str(item[0]) + "\t" + str(item[1]) + "\t" + str(item[2]) + "\t" + str(item[3]) + "\n")
FILE.close()	