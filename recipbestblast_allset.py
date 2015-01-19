#!/usr/bin/env python

import sys, os

def usage():
	print "Usage: recipbestblast_allset.py path2parsedBLASTresults"
	print "Need to update names list for running this with different SAGs"

if len(sys.argv) != 2:
	usage()
	exit()

nameslist=['AAA023D18', 'AAA023J06', 'AAA024D14', 'AAA027J17', 'AAA027L06', 'AAA027M14', 'AAA028A23', 'AAA028I14', 'AAA041L13', 'AAA044D11', 'AAA044N04', 'AAA278I18', 'AAA278O22', 'AB141P03']

path2results=sys.argv[1]

for name in nameslist:
	for name2 in nameslist:
		os.system("perl ~/Programs/reciprocal_blast_hit_parsing2.pl -i1 " + path2results+name+"_AAIblastresults.blast -i2 " + path2results+name2+"_AAIblastresults.blast -o " + path2results+name+"v"+name2+".rbb")