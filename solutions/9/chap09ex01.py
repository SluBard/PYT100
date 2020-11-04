#!/usr/bin/env python3
#
# A Solution For Chapter 9 Exercise 1
#
class Person:
    def __init__(self, fn = "Default", age = 21, sex = "Default"):
        self.name = fn
        self.age = age
        self.sex = sex

    def __str__(self):
        s = self.name + " "
        s += str(self.age) + " "
        s += self.sex
        return s

mom = Person("Sally", 76, "F") 
dad = Person("Arthur", 62, "M")
print(mom)
print(dad)
