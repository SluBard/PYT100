#!/usr/bin/env python3
#
# A Solution For Chapter 3 Exercise 1
#
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if num1 > num2:
    print(num1, "is the larger number")
elif num2 > num1:
    print(num2, "is the larger number")
else:
    print("the numbers are equal")
