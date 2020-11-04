#!/usr/bin/env python3
import sys

file = open(sys.argv[1], "r")

data = file.read(10)
while data: 
    print(data, end="")
    data = file.read(10) 
	
file.close()
