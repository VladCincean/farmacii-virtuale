#!/bin/bash

# 13. Sa se scrie un script shell care imi verifica
# daca un numar este prim sau nu.

n=""
while [ true ]; do
    echo "Indroduceti numarul n = "
    read n
    if expr $n + 0 > /dev/null 2>&1
	    then break
	    else echo "Nu ati introdus un numar valid" >&2
    fi
done

if [ $n -le 1 ]
    then echo "Nr. $n NU este prim."
    exit 1
fi
k=2
while [ $k -lt `expr $n / 2 + 1` ]; do
    if [ `expr $n % $k` -eq 0 ]
	then echo "Nr. $n NU este prim."
	exit 1
    fi
    k=`expr $k + 1`
done
echo "Nr. $n este prim."
exit 0
