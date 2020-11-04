#!/usr/bin/env python3
from sys import argv

file = open(argv[1], "r+")

for word in argv[2:]:
    for line in file:
        if line.startswith(word):
            print(line, end="")
    file.seek(0, 0)

file.close()
