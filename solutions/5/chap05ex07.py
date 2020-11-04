#!/usr/bin/env python3
#
# A Solution For Chapter 5 Exercise 7
#
def addn(theMap, number):
    for i in theMap.keys():
        theMap[i] = theMap[i] + number
	
h = { 'a':10, 'b':20, 'c':30 }
print(h)
addn(h, 10)
print(h)
