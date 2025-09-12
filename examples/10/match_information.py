#!/usr/bin/env python3
import re
while True:
    line = input("> ")
    if line == "q": break
    x = re.search('number ([0-9]+)', line)
    if x:
        print("Starting Position:", x.start())
        print(" Ending Position:", x.end())
        print("    The Number is:", x.group(1))
        print()
        print(x.group(0))
