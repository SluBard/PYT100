#!/usr/bin/env python3
#import platform
import os
#p = platform.popen("dir", "r")
p = os.popen("dir", "r")
data = p.readlines()
p.close()
for i in data:
    print(i, end="")
