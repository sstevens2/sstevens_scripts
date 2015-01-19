#!/usr/common/usg/languages/python/2.7.4/bin/python

import sys, os

def usage():
	print "Usage: comparebins.py newbinsdirectory oldbinsdirectory"


if len(sys.argv) !=3:
	usage()
	exit()


path2new=sys.argv[1]
path2old=sys.argv[2]

newlist=[]
oldlist=[]
oldlenlist=[]
countlist=[]
perclist=[]
perclist2=[]
matchlist=[]


for newf in os.listdir(path2new):
	if newf.split(".")[-1]=="txt":
		onew=open(path2new+newf, "rU")
		new=onew.readlines()
		onew.close()
		newlen=len(new)
		newlist.append(newf)
		templist=[]
		templist2=[]
		templist3=[]
		templist.append(newf)
		templist.append(newlen)
		templist2.append(newf)
		templist2.append(newlen)
		templist3.append(newf)
		templist3.append(newlen)
		for oldf in os.listdir(path2old):
			if oldf.split(".")[-1]=="txt":
				oold=open(path2old+oldf, "rU")
				old=oold.readlines()
				oldlen=len(old)
				if oldf not in oldlist:
					oldlist.append(oldf)
					oldlenlist.append(oldlen)
				#print newf, oldf
				cmatch=0
				onew.close()
				for line in new:
					if line in old:
						#print newf, oldf
						cmatch+=1
						match= newf, oldf
						if match not in matchlist:
							matchlist.append(match)
				templist.append(str(cmatch))
				perc=float(cmatch)/float(newlen)
				templist2.append(str(perc))
				perc2=float(cmatch)/float(oldlen)
				templist3.append(str(perc2))
		countlist.append(templist)
		perclist.append(templist2)
		perclist2.append(templist3)
#print newlist
#print oldlist
#print oldlenlist
#print countlist

output=open("bincomparison_count.txt", "w")
output.write("\t\t")
output2=open("bincomparison_percnew.txt", "w")
output2.write("\t\t")
output3=open("bincomparison_percold.txt", "w")
output3.write("\t\t")

for line in oldlist:
	output.write(line+"\t")
	output2.write(line+"\t")
	output3.write(line+"\t")
output.write("\n")
output2.write("\n")
output3.write("\n")
output.write("newname\tnewcontigs\t")
output2.write("newname\tnewcontigs\t")
output3.write("newname\tnewcontigs\t")
for line in oldlenlist:
	output.write(str(line)+"\t")
	output2.write(str(line)+"\t")
	output3.write(str(line)+"\t")
output.write("\n")
output2.write("\n")
output3.write("\n")

for line in countlist:
	for item in line:
		output.write(str(item)+"\t")
	output.write("\n")
output.close()


for line in perclist:
	for item in line:
		output2.write(str(item)+"\t")
	output2.write("\n")
output2.close()

for line in perclist2:
	for item in line:
		output3.write(str(item)+"\t")
	output3.write("\n")
output3.close()

output4=open("matchlist.txt", "w")
output4.write("newbin\toldbin\n")
for line in matchlist:
	output4.write(line[0]+"\t"+line[1]+"\n")
output4.close()