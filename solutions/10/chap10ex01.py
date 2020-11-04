#!/usr/bin/env python3
#
# A Solution For Chapter 10 Exercise 1
#
import re

while True:
    line = input("input an integer: ")
    ans = re.search("^[+-]?\d+$", line)
    if ans:
        print(line, " is all digits")
        if line[0] == '-':
            print("and is negative")
        else:
            print("and is positive")
    else:
        print(line, "is NOT all digits")
