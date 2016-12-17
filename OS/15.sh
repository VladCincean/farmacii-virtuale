#!/bin/bash

# 15. Sa se scrie un fisier de comenzi care primeste ca parametri
# perechi formate dintr-un nume de fisier si un numar k. Pentru fiecare
# pereche se vor afisa numele fisierului, numarul k si apoi primele
# k linii din fisier.

while [ $# -ne 0 ]; do
    f=$1
    k=$2
    echo "Numele fisierului: `basename $f`; k = $k"
    head --lines=$k $f
    shift
    shift
done

