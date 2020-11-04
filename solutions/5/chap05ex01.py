#!/usr/bin/env python3
#
# A Solution For Chapter 5 Exercise 1
#
def pos(li):
    result = []
    for element in li:
        if element > 0:
            result.append(element)
    return result

data = [5, -10, 10, -20, 30]
r = pos(data)
print(r)
