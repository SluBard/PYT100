#!/usr/bin/env python3
import re

line = "This string\nhas three\nlines\n"

x = re.search('g$', line, re.M)
if x:
    print("MATCH")
else:
    print("NO MATCH")
