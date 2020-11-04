#!/usr/bin/env python3
#
# A Solution For Chapter 8 Exercise 8
#
from sys import argv

if len(argv) == 1:
    print("need at least one file argument")
    exit(1)
	
total = False
argv.pop(0)
if argv[0].startswith("-t"):
    total = True
    argv.pop(0)
	
tlines = twords = tchars = 0
print("%-10s %5s %5s %5s" % ("FILE NAME", "LINES", "WORDS", "CHARS"))

for i in argv:
    f = open(i, "r")
    lines = words = chars = 0
    for line in f:
        lines += 1
        chars += len(line)
        data = line.split(None)
        words += len(data)
    print("%-10s %5d %5d %5d" % (i, lines, words, chars))
    twords = twords + words
    tchars = tchars + chars
    tlines = tlines + lines
	
if total:
    print("=" * 30)
    print("%-10s %5d %5d %5d" % ("TOTALS", tlines, twords, tchars))
