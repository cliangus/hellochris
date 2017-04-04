#!/usr/bin/env python

import sys

try:
	intake="input.txt"
	f=open(intake,'r')
	for line in f:
		array=line.split(":")
		fname=array[1].strip()
		open(fname+".python", "w").close()
except:
    print sys.exc_info()
    exit(2)
