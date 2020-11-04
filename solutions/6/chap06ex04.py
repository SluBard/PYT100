#!/usr/bin/python
#
# A Solution For Chapter 6 Exercise 4
#
from sys import argv

total = 0
for item in argv[1:]:
    total += float(item)

print(total / len(argv[1:]))
