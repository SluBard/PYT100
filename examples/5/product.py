#!/usr/bin/env python3
def product(begin, *items):
    res = begin
    for i in items:
        res *= i
    return res

result = product(5, 3, 4, 2)
print(result)
