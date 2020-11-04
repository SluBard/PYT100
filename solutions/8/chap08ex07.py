#!/usr/bin/env python3
#
# A Solution For Chapter 8 Exercise 7
#
from sys import argv

print("%-10s %5s %5s %5s" % ("FILE NAME", "LINES", "WORDS", "CHARS"))

for i in argv[1:]:
    f = open(i, "r")
    lines = words = chars = 0
    for line in f:
        lines += 1
        chars += len(line)
        data = line.split(None)
        words += len(data)
    print("%-10s %5d %5d %5d" % (i, lines, words, chars))
