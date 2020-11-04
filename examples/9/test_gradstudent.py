#!/usr/bin/env python3
from gradstudent import GradStudent

gs1 = GradStudent("James", "Anthropology", 4000)

print("MAJOR:", gs1.major())
print("NAME:", gs1.name())
print("STIPEND:", gs1.getstipend())

print(gs1)
