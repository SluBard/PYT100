#!/usr/bin/env python3
def thesum(param):
    total = 0
    for elem in param.values():
        total += elem
    return total

themap = { 'mike':10, 'jill':20, 'sam':30 }
x = thesum(themap)
print(x)
