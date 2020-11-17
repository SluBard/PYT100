#!/usr/bin/env python3
import os

data = [ "mike", "jane", "alice", "ruth" ]

p = os.popen("sort", "w")
for i in data:
    print(i, file=p)

p.close()
