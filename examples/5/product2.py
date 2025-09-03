#!/usr/bin/env python3
def product(*items, begin):
    res = begin
    for i in items:
        res *= i
    return res
result = product(3, 4, 2, begin = 5)
print(result)
product(3, 4, 2, 5)
