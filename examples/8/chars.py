#!/usr/bin/env python3
import sys
ct = 0
char = sys.stdin.read(1)
while char:
	ct += 1
	sys.stdout.write(char)
	char = sys.stdin.read(1)
print(ct)
