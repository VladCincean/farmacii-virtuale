#!/bin/bash

# Write a shell script that will create a file that contains a list of all the
# files from a folder given in the command line and its subfolders, that have
# none of the read, write and execute permission for the group. Then, for each
# file, grant read permission to the group.

if [ $# -gt 1 ]; then
    echo "Error. Too many parameters given."
    exit 1
fi

if [ $# -eq 0 ]; then
    echo "Error. No parameter given."
    exit 2
fi

if [ ! -d $1 ]; then
    echo "Error. Not a directory."
    exit 3
fi

find $1 -type f | while read F; do
    ls -l $F | cut -d' ' -f 1 | grep -q "\-...\-\-\-..."
    if [ $? -eq 0 ]; then
    	echo $F
    	chmod g+r $F
    fi
done | sort > result.txt
exit 0