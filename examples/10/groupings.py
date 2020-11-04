#!/usr/bin/env python3
import re
while True:
    line = input("Enter a string ")
    if line == "q": break
    x = re.search('www\.(a|b|c)\.(com|edu|org)',
                  line)
    if x:
        print("Groups:")
        print("\t#1:", x.group(1))
        print("\t#2:", x.group(2))
