#!/usr/bin/env python3
import re
while True:
    line = input("enter a string: ")
    if line == "q": break
    x = re.search('\d\d\s\d\d', line)
    if x:
        print("Match Found")
