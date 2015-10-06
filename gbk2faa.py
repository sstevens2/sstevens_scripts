#!/usr/bin/env python

import sys, os
from Bio import SeqIO

def usage():
	print "Usage: gbk2faa.py gbkfile"


if len(sys.argv) != 2:
	usage()
	exit()


gbk_filename = sys.argv[1]
faa_filename = os.path.splitext(sys.argv[1])[0]+'.faa'
input  = open(gbk_filename, "r")
output = open(faa_filename, "w")

for seq_record in SeqIO.parse(input, "genbank") :
    print "Dealing with GenBank record {0}".format(seq_record.id)
    for seq_feature in seq_record.features :
        if seq_feature.type=="CDS" :
            assert len(seq_feature.qualifiers['translation'])==1
            output.write(">{loctag}\n{seq}\n".format(
                   loctag=seq_feature.qualifiers['locus_tag'][0],seq=
                   seq_feature.qualifiers['translation'][0]))
output.close()
input.close()