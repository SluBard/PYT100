#!/usr/bin/env python3
def fun():
    f = 0
    s = 1
    def fibonacci():
        nonlocal f
        nonlocal s
        next = f
        f,s = s, f + s
        return next
    return fibonacci

result = fun()
print(result.__name__)
for i in range(20):
    print(result(), end = " ")
print()
