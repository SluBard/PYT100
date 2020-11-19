#!/usr/bin/env python3
#
# A Solution For Chapter 8 Exercise 1
#
fname1 = input("enter the name of the input file: ")
fname2 = input("enter the name of the output file: ")

fin = open(fname1, "r")
fout = open(fname2, "w")

while True:
    line = fin.readline()
    if not line:
        break
    fout.write(line)

fin.close()
fout.close()
