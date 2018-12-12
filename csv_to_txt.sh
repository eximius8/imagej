#!/bin/bash
  2 touch 'id.txt'
  3 fil ='id.txt'
  4 echo "" > id.txt 
  5 for f in *csv
  6 do
  7    echo -n $f >> id.txt
  8    tail -2 $f | head -1 >> id.txt
  9  done
 10  less id.txt 
