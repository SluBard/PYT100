#!/usr/bin/env python3
name = "michael"
age = 65
average = 92.65
income = 135000
print("|%-10s %5d %5.2f %15.2f|" % (name, age, average + 1,income)) #<-- Old Way
print("|{:<10s} {:5d} {:5.2f} {:15.2f}|".format(name,age,average+1,income))
print("|{:>10s} {:<5d} {:<5.2f} {:15.2f}|".format(name,age,average+1,income))
print("|{0:*<10s} {1:0>5d} {2:.2%} {3:0>15,.2f}|".format(name,age,(average+1)/100,income))

"""
Please see https://www.programiz.com/python-programming/methods/built-in/format
for more
"""
