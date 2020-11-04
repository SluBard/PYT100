#!/usr/bin/env python3
#
# A Solution For Chapter 5 Exercise 4
#
def deliver():
    return lambda x, y: x + y

f = deliver()
print(f(3,4))
print(f(10,20))
