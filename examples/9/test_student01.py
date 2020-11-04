#!/usr/bin/env python3
from student01 import Student
s1 = Student("Elizabeth", "Electrical Engineering")
print(s1.major())
print(s1.name())
s1.setmajor("Computer Science")
s1.setname("Beth")
print(s1.major())
print(s1.name())
