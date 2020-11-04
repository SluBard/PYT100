#!/usr/bin/env python3
def thesum(*args):
    total = 0
    print(type(args))
    for elem in args:
        total += elem
    return total
x = thesum(1,2,3,4,5)
print(x)
x = thesum(1,2,3)
print(x)
