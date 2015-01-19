#!/usr/bin/python

import sys, os, numpy, csv

"""compEst_makeIncompSetCluster.py
	This program takes a set of complete genomes.  Makes them incomplete, by values
	given, and then blasts all the genes and clusters them.
	INPUTS:
		Set of Genbank files(gbk_files)
		Size of blocks to delete(block_size), int
		Mean of Normal Dist. to use(ND_mean), float
		Stdv of Normal Dist. to use(ND_stdv), float
		Size of nuc seq to keep(ex. if nuc seq is partially deleted, keep > 100bp remains, minsize)
		Loc of required .py scripts(pyscr_loc)
	REQUIRED SETUP:
		Needs access to gbk_extractGeneInfo.py, convertseq(in Global Path on Zissou),
			filtersearchio5(also in global path on Zissou), parseMCLresults.py and fakeSAGcompleteness.py.
		Must be run in folder which contains the only gbk_files, ending in ".gb", not IMG format
	OUTPUTS:
		*.gb.fna - fasta nucleotide sequence extracted from the gbk_files
		*.tsv - tsv files containing the locus_tag, start, stop, strand, prot_seq, and prot_len 
			for each CDS from the gbk_files
		*.faa - fasta protein sequences for each CDS extracted from the gbk_files
		*.gb_incomp.fna -  fasta nucleotide sequence once made incomplete
		howComplValues.txt - text file that contains the new completeness values for the genomes
		*.fna.faa - fasta protein sequences for each CDS (that still exists after genome made incomplete)
		complete_allprotseq.fasta & .db - files for blasting all prot v all prot
		allprotVself.blast * .blast.id40.percqcov70 - blast output and filtered
		allprotVself.blast.id40.percqcov70.clusters & .clusters.sorted - clustered and parsed files
		namelist.txt -  for parsing cluster files by genome
	OTHER INFO:
		Sorted outputs into relevant folders
		All under "run_files"  - highly recommend renaming to avoid writing over if using same gbk_files
			"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: compEst_makeIncompSetCluster.py pyscr_loc ND_mean ND_stdv block_size minsize"
	print "INPUTS:"
	print "		Set of Genbank files(gbk_files)"
	print "		Size of blocks to delete(block_size), int"
	print "		Mean of Normal Dist. to use(ND_mean), float"
	print "		Stdv of Normal Dist. to use(ND_stdv), float"
	print "		Size of nuc seq to keep(ex. if nuc seq is partially deleted, keep > 100bp remains, minsize)"
	print "		Loc of required .py scripts(pyscr_loc)"
	print "	REQUIRED SETUP:"
	print "		Needs access to gbk_extractGeneInfo.py, convertseq(in Global Path on Zissou),"
	print "			filtersearchio5(also in global path on Zissou), parseMCLresults.py and fakeSAGcompleteness.py."
	print "		Must be run in folder which contains the only gbk_files, ending in .gb, not IMG format"

if len(sys.argv) != 6:
	usage()
	sys.exit(2)

#INPUT SETUP
pyscr_loc=sys.argv[1]
start_dir=os.getcwd()

	#Getting list of genome files to run on
genlist=[]
for file in os.listdir(start_dir):
	if file.endswith(".gb"):
		genlist.append(file)

#NDvalues
ND_mean=float(sys.argv[2])
ND_stdv=float(sys.argv[3])

block_size=sys.argv[4]
minsize=int(sys.argv[5])

log=open("runlog.txt", "w")

#MAKE FASTA AND TSV FILES FOR LATER
def fa_tsv_setup():
	os.system("for file in *.gb; do cat $file | seqconvert gb fa > $file.fna; done")
	os.system("for file in *.gb; do python "+pyscr_loc+"gbk_extractGeneInfo.py $file; done")

#GET INCOMPLETENESS VALUES
def rand_incomp():
	#Find how many genomes there are(numGs)
	numGs=len(genlist)
	#Make normal distribution of ND_mean and ND_stdv
	#Pull out a random numGs from the ND(cannot excede 100%),
	ND=numpy.random.normal(ND_mean, ND_stdv, numGs)
	#Check that this doesn't exceed 100, if so print error and quit
	for num in ND:
		if num > 100:
			print "VALUES IN DISTRIBUTION CANNOT EXCEED 100%, PLEASE MODIFY YOUR ND INPUT"
			log.write("VALUES IN DISTRIBUTION CANNOT EXCEED 100%, PLEASE MODIFY YOUR ND INPUT")
			sys.exit(2)
	return ND

#MAKE GENOMES INCOMPLETE
def make_incomp(normdist):
	#For each genome in file, take perc_comp and block_size and
	#	use fakeSAGcompleteness.py to make the incomplete genomes
	hc_output=open("howComplValues.txt","w") # file to show what the actual completeness values are
	hc_output.write("filename\tCompleteness\n")
	for genome in genlist:
		genname=genome+".fna"
		index=genlist.index(genome)
		hc_output.write(genname+"\t"+str(normdist[index])+"\n")
		print genname, normdist[index]
		log.write(genname+str(normdist[index])+"\n")
#		print "python "+pyscr_loc+"fakeSAGcompleteness.py "+genname+" "+str((.01*(100-normdist[index])))+" "+block_size
		os.system("python "+pyscr_loc+"fakeSAGcompleteness.py "+genname+" "+str((.01*(100-normdist[index])))+" "+block_size)
	hc_output.close()
	#files generated from this are the original name +_incomp.fna(unless fakeSAGcompleteness.py is altered)


#MAKE FASTAS OF LEFTOVER PROTEIN SEQS
#Check each protein in the incomplete genomes to see if meets size requirements
	#after portion is deleted, if kept, add to fasta file
def findRemProt():
	for genome in genlist:
		incomp_name=genome+"_incomp.fna"
		tsv_name=genome.split(".")[0]+".tsv"
		incomp=open(incomp_name, "rU")
		incomp.readline()
		fasta=incomp.read()
		#outfasta file with prot seqs
		outfaa=open(incomp_name+".faa", "w")
		tsvfile=open(tsv_name, "rU")
		tsvin=tsvfile.readlines()
		tsvin.pop(0)
		for row in tsvin:
			row=row.split("\t")
			nucseq=fasta[int(row[1]):int(row[2])]
			if nucseq.count('N') == 0: # if there are no N's, write to file
				outfaa.write(">"+row[0]+"\n")
				outfaa.write(row[4]+"\n")
			elif len(nucseq)-nucseq.count('N')>minsize: # if the number of N's makes it smaller than the minsize, go to next prot
				allNs= [i for i, ltr in enumerate(nucseq) if ltr == 'N'] #makes list of all indices for all N's
				if nucseq[0]=='N' and nucseq[-1]=='N': # go to next if beginning and end of seq are missing
					continue
				else:
					todel=int(numpy.ceil(len(allNs)/3.0)) # number of aa to delete
					if nucseq[-1]=='N': # if ends in N
						if row[3] =='1': # positive strand
							protseq=row[4][:-todel]
						else: # negative strand
							protseq=row[4][todel:]
						outfaa.write(">"+row[0]+"\n")
						outfaa.write(protseq+"\n")
					elif nucseq[0]=='N': # if begins in N
						if row[3] =='1': # positive strand
							protseq=row[4][todel:]
						else: # negative strand
							protseq=row[4][:-todel]
						outfaa.write(">"+row[0]+"\n")
						outfaa.write(protseq+"\n")
					elif nucseq[-1]!='N' and nucseq[0]!='N': # if begins and ends in N
						if allNs[0]>minsize: # is beginning seq bigger than min size
							tokeep1=int(numpy.floor(allNs[0]/3.0))
							if row[3] =='1': # positive strand
								protseq=row[4][:tokeep1]
							else: # negative strand
								protseq=row[4][-tokeep1:]
							outfaa.write(">"+row[0]+".1\n")
							outfaa.write(protseq+"\n")
						elif ((len(nucseq)-allNs[-1])-1)>minsize:
							tokeep2=int(numpy.floor((len(nucseq)-allNs[-1]-1)/3))
							if row[3] =='1': # positive strand
								protseq=row[4][-tokeep2:]
							else: # negative strand
								protseq=row[4][:tokeep2]
							outfaa.write(">"+row[0]+".2\n")
							outfaa.write(protseq+"\n")
		outfaa.close()
							

#BLAST AND CLUSTER
def blastNcluster():
	#Concatenate all the protein seqs left together
	os.system("cat *fna.faa > allprotseq.fasta")
	#Blast all v. all
	os.system("makeblastdb -in allprotseq.fasta -out allprotseq.db -dbtype prot")
	os.system("blastp -task blastp -query allprotseq.fasta -db allprotseq.db -out allprotVself.blast -evalue 0.001")
	os.system("filtersearchio5 -qcoverage 70 -identity 40 -format 8 < allprotVself.blast > allprotVself.blast.id40.percqcov70")
	#Cluster
	os.system("mcxdeblast --score=r --m9 --line-mode=abc --rcut=1.0 --out=- allprotVself.blast.id40.percqcov70 | mcl - --abc -o allprotVself.blast.id40.percqcov70.clusters")
	#Parse Cluster results
	#Get locus tag names to parse clusters
	namefile=open("namelist.txt", "w")
	for genome in genlist:
		file=open(genome.split(".gb")[0]+".tsv", "rU")
		filel=file.readlines()
		namefile.write(filel[1].split("_")[0]+"\n")
	namefile.close()
	#Run parsing program
	os.system("python "+pyscr_loc+"parseMCLclusters.py allprotVself.blast.id40.percqcov70.clusters namelist.txt")

#clean up files
def cleanup():
	#make folder to keep run files in
	os.system("mkdir run_files")
	#make folder to keep gb within runfiles
	os.system("mkdir run_files/gb")
	os.system("mv *.gb run_files/gb")
	#make folder to keep tsv within runfiles
	os.system("mkdir run_files/tsv")
	os.system("mv *.tsv run_files/tsv")
	#make folder to keep complete fna and faa within runfiles
	os.system("mkdir run_files/fnafaa")
	os.system("mv *.fna run_files/fnafaa")
	os.system("mv *.faa run_files/fnafaa")
	#make text file that gives run information within runfiles
	infofile=open("runinfo.txt", "w")
	for item in sys.argv:
		infofile.write(item +" ")
	infofile.write("\n")
	infofile.write("OUTPUTS:\n")
	infofile.write("		*.gb.fna - fasta nucleotide sequence extracted from the gbk_files\n")
	infofile.write("		*.tsv - tsv files containing the locus_tag, start, stop, strand, prot_seq, and prot_len \n")
	infofile.write("			for each CDS from the gbk_files\n")
	infofile.write("		*.faa - fasta protein sequences for each CDS extracted from the gbk_files\n")
	infofile.write("		*.gb_incomp.fna -  fasta nucleotide sequence once made incomplete\n")
	infofile.write("		howComplValues.txt - text file that contains the new completeness values for the genomes\n")
	infofile.write("		*.fna.faa - fasta protein sequences for each CDS (that still exists after genome made incomplete)\n")
	infofile.write("		complete_allprotseq.fasta & .db - files for blasting all prot v all prot\n")
	infofile.write("		allprotVself.blast * .blast.id40.percqcov70 - blast output and filtered\n")
	infofile.write("		allprotVself.blast.id40.percqcov70.clusters & .clusters.sorted - clustered and parsed files\n")
	infofile.write("		namelist.txt -  for parsing cluster files by genome\n")
	infofile.write("	OTHER INFO:\n")
	infofile.write("		Sorted outputs into relevant folders\n")
	infofile.write("		All under run_files  - highly recommend renaming to avoid writing over if using same gbk_files\n")
	infofile.close()
	os.system("mv runinfo.txt run_files")
	os.system("mv howComplValues.txt run_files")
	os.system("mv runlog.txt run_files")
	#make folder for blastoutput files within runfiles
	os.system("mkdir run_files/blastout")
	os.system("mv allprotVself.* run_files/blastout")
	os.system("mv allprotseq.* run_files/blastout")
	os.system("mv namelist.txt run_files/blastout")
	

###ACTUAL RUN OF FUNCTIONS
print "Starting file setup"
log.write("Starting file setup\n")
fa_tsv_setup()
print "Finding Normal distribution"
log.write("Finding Normal distribution\n")
normdist=rand_incomp()
print "Making genomes incomplete"
log.write("Making genomes incomplete\n")
make_incomp(normdist)
print "Finding remaining proteins"
log.write("Finding remaining protein\n")
findRemProt()
print "Blasting and Clustering"
log.write("Blasting and Clustering\n")
blastNcluster()
print "Cleaning up Output"
log.write("Cleaning up Output\n")
cleanup()
log.close()
