#!/usr/bin/env python3
import sys
ct = lines = 0
file = open(sys.argv[1], "r")

while True:
    line = file.readline()
    if not line:
        break
    ct += len(line)
    lines += 1
    
file.close()
print("Characters:", ct, " Lines:", lines)
