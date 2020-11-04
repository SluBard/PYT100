#!/usr/bin/env python3
x = "Capital of Mississippi is Jackson"
pos = x.find("is")
print(pos)
print(x.find("is", pos + 1))
print(x.find("is", 8, 12))
print()

x = "1 1 1 1abc"
y = x.replace("1","0")
print(y)
y = x.replace("1", "0", 2)
print(y)
print()

list = x.split(' ')
print(x)
print(list)
