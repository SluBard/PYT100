#!/usr/bin/env python3
def cube(x):
    return x * x * x

data = [2, 4, 6, 8]
cubed_data = map(cube, data)
print(type(cubed_data))
print(cubed_data)
for value in cubed_data:
    print(value, end=" ")
print("\n")

cubed_data = list(map(cube, data))
print(cubed_data)
