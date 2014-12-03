#!/usr/bin/python

#Sarah Stevens
#sstevens2@wisc.edu

import sys, os, random


def usage():
	print "Usage: fakeSAGcompleteness.py complete_genome(name must end in .fna) percent2delete(in decimal) blocksize2delete(an integer)"
	print "This program deletes random portions of a !COMPLETE! genome and makes these into separated contigs."
	print "It is meant to be used to make genomes of known random incompletion(SAG like) for testing genome completion scripts."
	print "Rounds off bases to delete to nearest whole number, outputname gives exact perc though, to 4 decimals"
	print "Warning! large percentages and smaller block sizes will take longer, as will larger genomes"
	
if len(sys.argv) != 4:
	usage()
	exit()

#Reading in file
genomefile=open(sys.argv[1], "rU")
contig_name=genomefile.readline()
genome=genomefile.read()
genomefile.close()
genome=genome.replace("\n", "")
#percent to delete
perc2del=float(sys.argv[2])
#block size
b_size=int(sys.argv[3])
#size of genome
g_size=len(genome)

#calculating the number of bases that need to be deleted, rounded
bases2del=int(round(g_size*perc2del))
#calculating what the final percentage deleted will be, after rounding
new_perc=int(round(g_size*perc2del))/float(g_size)
#calculating how many blocks need to be deleted
blocks2del=bases2del/float(b_size)
#print blocks2del


#finds random location to delete, if not previously deleted(aka on the delbases list)
def findrandomloc(glenth):
	loc=random.randint(0, glenth)
	return loc

#deletes all fullsize blocks, doesn't count 'N' bases again
while (bases2del-genome.count('N')) > b_size:
	position=findrandomloc(g_size)
	if (g_size-position) > b_size:
		genome=genome[:position]+"N"*b_size+genome[position+b_size:]
	else:
		genome=genome[:position]+"N"*(g_size-position)
		todel=b_size-(g_size-position)
		genome="N"*todel+genome[todel:]
#print len(genome)
#	print genome.count('N')

#print (bases2del-genome.count('N')), genome.count('N')/float(g_size)

#deletes block of the size of bases needed to get all deleted, but again, doesn't count if deleted is an 'N'
while (bases2del-genome.count('N')) != 0:
	position=findrandomloc(g_size)
	deletesize=bases2del-genome.count('N')
	if (g_size-position) > deletesize:
		genome=genome[:position]+"N"*deletesize+genome[position+deletesize:]
	else:
		genome=genome[:position]+"N"*(g_size-position)
		todel=deletesize-(g_size-position)
		genome="N"*todel+genome[todel:]
#print len(genome)
#	print genome.count('N')

#print (bases2del-genome.count('N')), genome.count('N')/float(g_size)

#makes output and writes to it
# NEED TO FINISH THIS!
percent=str(round(genome.count('N')/float(g_size),5))[:6]

outname=sys.argv[1].split(".fna")[0]+"_block"+sys.argv[3]+"_perc"+percent+".fna"
output=open(outname,"w")
output.write(contig_name)
output.write(genome)
output.close()

"""
#Random testing to check if 'N' counting and to make sure size was same after 'N' insertion
testing
string="NNNNNAAACCCCTTTTCCCC"
print len(string)-string.count('N')
more testing
string2="AAAAAAAAAATTTTTTTTTTAAAAAAAAAA"
startpos=10
size=10
newstring=string2[:startpos]+'N'*size+string2[startpos+size:]
print len(string2), len(newstring)
"""
