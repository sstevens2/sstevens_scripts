#!/usr/bin/env python

import sys, os, re

list = ["genome1_locus2", "genome2_locus2", "genome1_locus3"]

for item in list:
	match = re.match("genome1", item)
	if match != None:
		print match