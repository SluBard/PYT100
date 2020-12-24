#!/usr/bin/env python3
#
# A Solution For Chapter 10 Exercise 2
#
import re

while True:
    line = input("input an floating point number: ")
    ans = re.search("^[+-]?\d*\.\d+$",line) #first d* was d+
    if ans:
        print(line, " is a floating point number")
        if line[0] == '-':
            print("and is negative")
        else:
            print("and is positive")
    else:
        print(line, "is NOT a floating point number")
