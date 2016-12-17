#!/bin/bash

# 11. Sa se scrie un script shell care imi listeaza continutul directorului curent.
# Se vor face trei afisari: una sortata dupa numele fisierelor, alta dupa timpul
# ultimului acces la ele si cea de-a treia, dupa dimensiunea in bytes a acestora.

D=. #directorul curent

echo "### Dupa nume:"
ls -1 | sort
echo "### Dupa timpul ultimului acces:"
ls -t -1
echo "### Dupa dimensiunea fisierelor:"
ls -S -1
