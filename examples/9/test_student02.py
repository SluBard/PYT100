#!/usr/bin/env python3
from student02 import Student
s1 = Student("Elizabeth", "Electrical Engineering")
print("Length:", len(s1))
s1.setmajor("Accounting")
print("Length:", len(s1))
s1 = Student("Joe", "Teaching")
print(s1)
