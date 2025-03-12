#!/usr/bin/env python3

# from Python 3.3 and prior:
#import platform
#
#data = [ "mike", "jane", "alice", "ruth" ]
#
#p = platform.popen("sort", "w")
#for i in data:
#    print(i, file=p)
#
#p.close()

# from python 3.4 and up:
import subprocess

data = [ "mike", "jane", "alice", "ruth" ]

p = subprocess.Popen(["sort"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
data_stdout, data_stderr = p.communicate(input="\n".join(data))
print(data_stdout)
