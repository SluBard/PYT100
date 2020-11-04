#!/usr/bin/env python3
import re
while True:
    line = input("enter a string: ")
    if line == "q": break
    x = re.search('the', line)
    print(type(x))
    if x:
        print("'the' Found")
    else:
        print("No Match found")
