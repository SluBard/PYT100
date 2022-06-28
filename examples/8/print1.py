#!/usr/bin/env python3
import sys
f = open("output", "w")
#f=sys.stdout

while True:
    data = input("Enter data ('q' to exit): ")
    if data == "q":
        break
    print(data, file=f)
    
f.close()    
