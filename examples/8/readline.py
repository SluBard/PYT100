#!/usr/bin/env python3
import sys
line = sys.stdin.readline()
num = 1
while line:
	print("%4d %s" % (num, line), end="")
	line = sys.stdin.readline()
	num += 1
