#!/usr/common/usg/languages/python/2.7.4/bin/python

import sys

"""parse_phylosift_sts.py: takes a sequence_taxa_summary.txt file from the program phyosift (run on only one bin/genome)
	and uses a cutoff probability and percentage to determine the taxonomy of that bin/genome"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: parse_phylosift_sts.py inputfile  cutoffprob. cutoffpercentage outnameprefix BacteriaArchaeaMarkersOnly(True/False?)"
	print "Example: parse_phylosift_sts.py sequence_taxa_summary.txt .90 .70 sts_mygenome.txt True"
	print "The cutoffprob. and cutoffperc. need to be in decimal form, not percentages"
	print "Must use 'True' or 'False' exactly for using only the Bacterial/Archaeal Marker genes"

if len(sys.argv) !=6:
	usage()
	exit()

#Bring in the inputs and set up output
inputfile=open(sys.argv[1], "rU")
list1 =inputfile.readlines()
co_prob=float(sys.argv[2])
co_perc=float(sys.argv[3])
outname=sys.argv[4]
concatonly=bool(False)
if sys.argv[4] == "True":
	concatonly=bool(True)
outputfile=open(outname+".prob+"+str(co_prob)+".perc"+str(co_perc)+".txt", "w")


def prob_check(list2check): #Removes all lines below the co_prob or that have 'no rank', returns list with	all fines above or equal to the co_prob
	outlist=[]
	#checklist=[]
	for line in list2check:
		if not (float(line[5]) < co_prob):
			if not (line[3] == 'no rank'):
				#checklist.append(line[5])
				outlist.append(line)
	#print checklist
	return outlist

def match_check(list2check, rank2check): #Function for checking specific level of taxonomy for matching, returns if matches above the co_perc.  and if True, what the match is
	ranklist = []
	markerlist=[]
	#adds all the lines that match the rank to ranklist
	for line in list2check:
		if line[3] == rank2check:
			ranklist.append(line)
			markerlist.append(line[-1])
	rankcount=[]
	#checks all possible combos for matching ranks with that line
	for line in ranklist:
		count=(len(line[1].split("."))/2)
		#count=0
		for line2 in ranklist:
			if line != line2:
				if line[4] == line2[4]:
					#count+=1
					count=count+(len(line2[1].split("."))/2)
		rankcount.append(count)
	num_matches= max(rankcount)
	total=len(rankcount)
	bm_index=rankcount.index(max(rankcount))
	bm_name =ranklist[bm_index][4]
	index=0
	mmlist=[]
	for num in rankcount:
		if num != max(rankcount):
			mmlist.append(ranklist[index][1])
		index+=1
	#print num_matches, total,  (float(num_matches)/float(total)), co_perc
	if total <= 1:
		return False, mmlist
	if (float(num_matches)/float(total)) < co_perc:
		return False, mmlist
	else:
		outputfile.write(rank2check+": "+bm_name+"\n")
		print(bm_name)
		return True, mmlist

def trueMatch(matchTF): #terminates program if matchTF is false
	if matchTF == False:
		outputfile.close()
		sys.exit()
		
def mremover(list2check, mlist): #removes markers ruled out from previous levels
	outputlist=[]
	for line in list2check:
			if (line[1] not in mlist) and (line[1] not in outputlist):
				if line not in outputlist:
					outputlist.append(line)
	return outputlist

def checkrank(list2check, rank): #checks that all the makers have that rank, returns list of markers to remove
	missmarklist=[]
	rankmatchlist=[]
	for line in list2check:
		if (line[3] == rank):
			rankmatchlist.append(line[1])
	for line in list2check:
		if (line[1] not in rankmatchlist) and (line[1] not in missmarklist):
			missmarklist.append(line[1])
	return missmarklist

def bacterialmonly(list2check):
	outputlist=[]
	for line in list2check:
		if line[-1].split("\n")[0] == "concat" or line[-1].split("\n")[0] == "16s_reps_bac":
			outputlist.append(line)
	return outputlist

#Sort lines of inputfile into lists to be used by prob_check
list2=[]
for line in list1:
	list2.append(line.split("\t"))
inputfile.close()
#print(list2[0])
list2.pop(0)


#run prob_check on the list
prob_list=prob_check(list2)
#print prob_list
#run match-check on each level
taxon_ranks=['superkingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species']
for rank in taxon_ranks:
	if len(prob_list) != 0:
		if concatonly == True:
			prob_list=bacterialmonly(prob_list)
		norankmlist=checkrank(prob_list, rank)
		prob_list=mremover(prob_list,norankmlist)
		matchTF, mismlist =match_check(prob_list, rank)
	if len(mismlist) != 0:
		prob_list=mremover(prob_list, mismlist)
	trueMatch(matchTF)
