#!/usr/bin/env python3
import re
while True:
    line = input("Enter a string ")
    if line == "q": break
    total = 0
    x = re.split('\D+', line)

    if x:
        print("Split into a list of length", len(x))
        for number in x:
            if len(number) != 0:
                total += int(number)
        print(total)
