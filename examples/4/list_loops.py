#!/usr/bin/env python3
grades = ["A", "B", "C", "D", "F"]
ranges = ["90 - 100", "80 - 89", "70 - 79",
          "60 - 69", "00 - 59"]
for grade in grades:
    print(grade)
print()

for i, grade in enumerate(grades):
    print(i + 1, ":", grade)
print()

for index, grade in enumerate(grades):
    print(grade, ":", ranges[index])
