#!/usr/bin/env python3
import re
while True:
    line = input("enter a string: ")
    if line == "q": break
    x = re.search('\+\*', line)
    if x:
        print("'+*' Found")
