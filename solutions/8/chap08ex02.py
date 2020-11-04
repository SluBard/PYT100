#!/usr/bin/env python3
#
# A Solution For Chapter 8 Exercise 2
#
import sys

if len(sys.argv) != 3:
    print("usage: inputfile outptfile")
    exit(1)
    
fin = open(sys.argv[1], "r")
fout = open(sys.argv[2], "w")

while True:
    line = fin.readline()
    if not line:
        break
    fout.write(line)

fin.close()
fout.close()
