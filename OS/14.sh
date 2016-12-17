#!/bin/bash

# 14. Se va srie un script shell care compara continutul
# a doua fisiere text si va tipari primele 5 linii diferite

if [ ! -f $1 ]
    then echo $1 "nu este fisier"
    exit 1
fi
if [ ! -f $2 ]
    then echo $2 "nu este fisier"
    exit 1
fi

echo "Primele 5 linii diferite din `basename $1`:"
comm -23 --nocheck-order $1 $2 | head -n 5
echo "----------------------------------"
echo "Primele 5 linii diferite din `basename $2`:"
comm -13 --nocheck-order $1 $2 | head -n 5
