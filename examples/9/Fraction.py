#!/usr/bin/env python3
class Fraction:
    def __init__(self, n, d):
        self.n =  n
        self.d = d
    def __str__(self):
        return str(self.n) + "/" + str(self.d)
    def __lt__(self, other):
        left = self.n / self.d
        right = other.n / other.d
        return left < right
    def __mul__(self, other):
        num = self.n * other.n
        den = self.d * other.d
        return Fraction(num, den)
