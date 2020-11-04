#!/usr/bin/env python3
import sys
lines = sys.stdin.readlines()
num = 1
for line in lines:
	print("%4d %s" % (num, line), end="")
	num += 1
