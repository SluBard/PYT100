#!/usr/bin/env python3
#
# A Solution For Chapter 10 Exercise 3
#
import re

while True:
    line = input("input a line: NNAA ... DESC: ")
    ans = re.search("^(\d\d)([A-Z][A-Z])\s+(.*)$", line)
    if ans:
        print("NUMBER IS", ans.group(1))
        print("ALPHA IS", ans.group(2))
        print("DESC IS", ans.group(3))
    else:
        print(line, "DOES NOT MATCH NNAA ... DESC")
