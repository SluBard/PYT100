#!/usr/bin/env python3
import sys

try:
    file = open(sys.argv[1], "r")
except OSError as err:
    print(type(err))
    print(err)
    exit(1)
finally:
    print("IN FINALLY")

num = 1
line = file.readline()
while line:
    print(str(num) + "\t" + line, end="")
    num += 1
    line = file.readline()

file.close()
