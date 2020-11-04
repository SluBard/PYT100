#!/usr/bin/env python3
import re
while True:
    line = input("Enter a string ")
    if line == "q": break
    x = re.search('mike|chris|susan', line)
    if x: print("Match Found")
