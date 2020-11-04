#!/usr/bin/env python3
import os

files = os.listdir(".")
ct = 0

for file in files:
    f = open(file, "r")
    lines = f.readlines()
    ct += len(lines)
    f.close()

print(ct)
