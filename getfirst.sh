#!/bin/bash
if [ -d "output/" ]; then rm -rf output/; fi
mkdir -p output
intake="input.txt"
while IFS=":" read -ra line
do
	echo ${line[0]} >> ./output/${line[0]}.bash
done < "$intake"
RETVAL=$?
