#!/usr/bin/env python

#Usage 

import sys, os


def usage():
	print "make_primers.py"

filename = "primer3.input.txt"
FILE = open(filename,"w")


if not len(sys.argv) == 1:
	usage()
	exit(2)

#def findprimers(file, whereNs):

for filename in os.listdir(os.getcwd()):
		if str(filename).endswith('.fas') or str(filename).endswith('.TXT'):
			newfile = open(filename, "r")
			seqfile=newfile.readlines()
			seqfile2=seqfile[0]
			splitseqfile2 = seqfile2.splitlines()
			seq = ''
			splitseqfile2.pop(0)
			print splitseqfile2
			for item in splitseqfile2:
				seq= seq + item
			seqlist = list(seq)
			index = 0
			Nstart = len(seqlist)
			Nend = 0
			nseqlist = []
			for char in seqlist:
				if char == 'N' and index<Nstart:
					Nstart=index
				elif char == 'N' and index>Nend:
					Nend=index
				index= index + 1
			Nlength = Nend-Nstart+1
			print Nstart, Nlength
			nseq= ''
			if Nstart>200:
				cutoff = Nstart-200
				for item in range(200+Nlength+200):
					nseqlist.append(seqlist[cutoff+item])
				for char in nseqlist:
					nseq = nseq + char
			Nlength = Nlength + 150
			strNlength = str(Nlength)
			print 'SEQUENCE_ID=' + filename + '\nSEQUENCE_TEMPLATE=' + nseq + '\nSEQUENCE_TARGET=150,'+ strNlength + '\nPRIMER_TASK=pick_sequencing_primers\nPRIMER_LIBERAL_BASE=1\nP3_FILE_FLAG=1\n=\n'
			FILE.write('SEQUENCE_ID=' + filename + '\nSEQUENCE_TEMPLATE=' + nseq + '\nSEQUENCE_TARGET=150,'+ strNlength + '\nPRIMER_TASK=pick_sequencing_primers\nPRIMER_LIBERAL_BASE=1\nP3_FILE_FLAG=1\n=\n')
	
			
FILE.close()	
	
	
os.system("primer3_core -format_output < primer3.input.txt")
