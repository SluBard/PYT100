#!/usr/bin/env python3
#import platform
import os

data = [ "mike", "jane", "alice", "ruth" ]

#p = platform.popen("sort", "w")
p = os.popen("sort", "w")
for i in data:
    print(i, file=p)

p.close()
