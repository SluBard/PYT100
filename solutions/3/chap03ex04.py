#!/usr/bin/env python3
#
# A Solution For Chapter 3 Exercise 4
#
low = int(input("enter a lower limit: "))
high = int(input("enter an upper limit: "))
step = int(input("enter a step size: "))

for i in range(low, high, step):
    print(i)
