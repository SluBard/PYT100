#!/usr/bin/env python3
import sys

file = open(sys.argv[1], "r")

lines = file.readlines()
file.close()

for line in lines:
    print(line, end="")
