#!/usr/bin/env python3
#
# A Solution For Chapter 8 Exercise 5
#
import sys

if len(sys.argv) != 3:
    print("Need two argument files")
    exit(1)

f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")

s1 = set()
for line in f1:
    s1.add(line)

s2 = set()
for line in f2:
    s2.add(line)

s3 = s1 & s2
for line in  s3:
    print(line, end="")
