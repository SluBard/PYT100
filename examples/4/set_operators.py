#!/usr/bin/env python3
a = set('efgy')
b = set('exyz')
print("Set a:", a)
print("Set b: ", b)

print("a | b:", a | b )  # union
print("a & b:", a & b )  # intersection
print("a - b:", a - b )  # difference
print("b - a:", b - a )  # difference
print("a ^ b:", a ^ b )  # symmetric difference
