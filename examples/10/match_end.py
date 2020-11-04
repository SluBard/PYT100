#!/usr/bin/env python3
import re
while True:
    line = input("> ")
    if line == "q": break
    x = re.search('\d{2,5}$', line)
    if x: print("Ends with 2 to 5 digits")
