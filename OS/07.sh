#!/bin/bash

# 7. Sa se scrie un script shell care primeste ca parametru un nume de director
# si va determina numarul total de linii din toate fisierele text din
# acest director si din toate subdirectoarele acestuia. Se presupune ca
# orice director va contine doar fisiere text.

D=$1

if [ $D = "" ]; then
    D=.
fi

if [ ! -d $D ]; then
    echo "Invalid directory"
    exit 1
fi

find $D -type f | while read F; do
    a=`wc -l $F | cut -d' ' -f1`
    echo "`basename $F` are $a linii."
done

