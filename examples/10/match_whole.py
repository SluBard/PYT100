#!/usr/bin/env python3
import re
while True:
    line = input("> ")
    if line == "q": break
    x = re.search(r'^\d{5}(-\d{4})?$', line)
    if x: print("Is a ZipCode")
