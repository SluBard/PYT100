#!/usr/bin/env python3
#
# A Solution For Chapter 8 Exercise 4
#
import sys
import os
import time

if len(sys.argv) != 3:
    print("usage: " + sys.argv[0], "dir_name size")
    exit(1)

files =  os.listdir(sys.argv[1])
os.chdir(sys.argv[1])

for file in files:
    data = os.stat(file)
    if data[6] > int(sys.argv[2]):
        print(file, data[6], time.ctime(data[8]));
