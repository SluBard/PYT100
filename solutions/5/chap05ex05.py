#!/usr/bin/env python3
#
# A Solution For Chapter 5 Exercise 5
#
def reverse(param):
    lis = list(param)
    lis.reverse()
    return lis

def sort(param):
    lis = list(param)
    lis.sort()
    return lis

values = [10,40,30,20,5]
print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
print(values)
