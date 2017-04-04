#!/bin/bash
intake="input.txt"
while IFS=":" read -ra line
do
	touch ${line[0]}.bash
done < "$intake"
RETVAL=$?
