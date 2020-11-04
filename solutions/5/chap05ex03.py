#!/usr/bin/env python3
#
# A Solution For Chapter 5 Exercise 3
#
def deliver():
    def addthem(a, b):
        return a + b
    return addthem

f = deliver()
print(f(3,4))
print(f(10,20))
