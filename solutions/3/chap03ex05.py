#!/usr/bin/env python3
#
# A Solution For Chapter 3 Exercise 5
#
for i in range(50):
    print(("%3d " % (i)),end="")
    if i % 10 == 9:
        print()
