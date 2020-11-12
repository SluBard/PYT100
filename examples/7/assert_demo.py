#!/usr/bin/env python3
def findmax(a,b):
    max= 0
    if a < b:
        max= b
    if b < a:
        max= a
    assert (max == a or max == b)
    return max;

try:
    print(findmax(3,3))
    print(findmax(2,3))
    print(findmax(3,2))

except AssertionError:
    print("Assertion Failed:")
