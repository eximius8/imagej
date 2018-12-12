#!/bin/bash
touch 'id.txt'
echo "" > id.txt 
for f in *csv
 do
    echo -n $f >> id.txt
    tail -2 $f | head -1 >> id.txt
 done
less id.txt 
