#!/usr/bin/env python3
import re
while True:
    line = input("Enter a string ")
    if line == "q": break
    x = re.search('\d{5}', line)
    if x: print("Match Found")
