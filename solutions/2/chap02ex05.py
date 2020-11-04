#!/usr/bin/env python3
#
# A Solution For Chapter 2 Exercise 5
#
data = input("enter a string: ")
x = data.isalpha()

print("ALL ALPHA CHARS   :", x)
print("ENDS WITH A PERIOD:", data.endswith("."))
print("x IN THE STRING   :", 'x' in data)
print("LENGTH OF STRING  :", len(data))

#
#	The string has no newline when you use input()
#
newstring = data.replace('e', 'E')
print(newstring)
