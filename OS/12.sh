#!/bin/bash

# 12. Sa se scrie un script shell care va redenumi toate
# fisierele txt din directorul curent si din toate
# subdirectoarele acestuia, dandu-le extensia .ascii.

D=. #directorul curent

find $D -type f | grep ".txt$" | while read F; do
    mv $F ${F}.ascii
done
