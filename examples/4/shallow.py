#!/usr/bin/env python3
a = [ 1, 2, 3 ]    # create a list
b = a              # shallow copy
print(id(a))
print(id(b))

a.append(10)
print(a)
print(b)
