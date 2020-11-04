#!/usr/bin/env python3
import platform
p = platform.popen("dir", "r")
data = p.readlines()
p.close()
for i in data:
    print(i, end="")
