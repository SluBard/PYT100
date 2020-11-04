#!/usr/bin/env python3
a = [ 1, 2, 3 ]    # create a list
b = list(a)        # deep copy
print(id(a))
print(id(b))

a.append(10)
print(a)
print(b)
