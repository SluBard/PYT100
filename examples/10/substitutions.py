#!/usr/bin/env python3
import re
while True:
    line = input("Enter a string ")
    if line == "q": break
    result = re.sub('the', 'THE', line)
    print(result)
    print(line)
