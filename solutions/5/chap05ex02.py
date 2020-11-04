#!/usr/bin/env python3
#
# A Solution For Chapter 5 Exercise 2
#
def pos(*t, num=0):
    result = 0
    for element in t:
        if element > num:
            result += 1
    return result

limit = 20
res = pos(5, -10, 10, -20, 30, num=limit)
print("There are %d values greater than %d" % (res, limit))
