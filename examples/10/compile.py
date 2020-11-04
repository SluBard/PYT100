#!/usr/bin/env python3
import re

comp = re.compile( '((.*) (.*)) (.*)' )

while True:
    line = input("enter a string: ")
    if line == "q": break
    x = comp.match(line)
    if x:
        print("Start:End ", x.start(),":", x.end())
        print("Group1:", x.group(1))
        print("Group2:", x.group(2))
        print("Group3:", x.group(3))
        print("Group4:", x.group(4))
