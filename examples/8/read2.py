#!/usr/bin/env python3
import sys

lines = 0
file = open(sys.argv[1], "r")

line = file.readline()
while line:
    lines += 1
    line = file.readline()
file.close()
print(lines)
