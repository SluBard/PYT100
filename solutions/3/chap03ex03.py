#!/usr/bin/env python3
#
# A Solution For Chapter 3 Exercise 3
#
line = input("enter some numbers: ")
numbers = line.split(" ")

for num in numbers:
    num = int(num)
    if num > 0:
        print(num)
