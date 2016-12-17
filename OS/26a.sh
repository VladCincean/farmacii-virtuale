#!/bin/bash

# Write a shell script that will monitor all the folders given in the command
# and notify the user if a certain file will be created inside them (the name
# of the file will be read from keyboard).

if [ $# -eq 0 ]; then
    echo "Error. No command line arguments given."
    exit 1
fi

read -p "name of the file: " F

for D in $@; do
    ls -l $D | grep "^\-.\+" | grep -q "$F$"
    if [ $? -eq 0 ]; then
	echo "There already exists a file named '$F' in directory '$D'"
	exit 0
    fi
done
echo "Started monitoring..."
echo "You can press Ctrl-C to cancel..."


while [ true ]; do
    for D in $@; do
	ls -l $D | grep "^\-.\+" | grep -q "$F$"
	if [ $? -eq 0 ]; then
	    echo "File '$F' just created in directory '$D'"
	    break 2
	fi
    done
    sleep 1
done
exit 0