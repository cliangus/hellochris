#!/usr/bin/env python

import sys

try:
	intake="input.txt"
	f=open(intake,'r')
	for line in f:
		array=line.split(":")
		fname=array[1].strip()
		target=open("./output/"+fname+".python", "w")
		target.write(fname)
		target.close
except:
    print sys.exc_info()
    exit(2)
