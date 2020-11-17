#!/usr/bin/env python3
import os
p = os.popen("dir", "r")
data = p.readlines()
p.close()
for i in data:
    print(i, end="")
