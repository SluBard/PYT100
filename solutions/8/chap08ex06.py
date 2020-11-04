#!/usr/bin/env python3
#
# A Solution For Chapter 8 Exercise 6
#
import sys

hash = { } 

for filename in sys.argv[1:]:
    f1 = open(filename, "r")
    for line in f1:
        line = line.strip()
        if line in hash:
            hash[line] += 1
        else:
            hash[line] = 1

names = list(hash.keys())
names.sort()

for i in names:
    print("%-10s%4d" % (i, hash[i]))
