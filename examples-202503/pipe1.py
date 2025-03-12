#!/usr/bin/env python3

# from Python 3.3 and before:
# import platform
# p = platform.popen("dir","r")
# data = p.readlines()
# p.close()
# for i in data:
#     print(i, end="")

# from python 3.4 and up:
import subprocess

p = subprocess.Popen(["dir"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
data_stdout, data_stderr = p.communicate()
print(data_stdout)
