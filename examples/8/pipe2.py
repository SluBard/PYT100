#!/usr/bin/env python3
import platform #os

data = [ "mike", "jane", "alice", "ruth" ]

p = platform.popen("sort", "w")
for i in data:
    print(i, file=p)

p.close()
