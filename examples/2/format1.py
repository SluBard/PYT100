#!/usr/bin/env python3
name = "michael"
age = 65
average = 92.65
print("|%s %d %f|" % (name, age, average)) # <-- Don't do it this way!
print("|{:s} {:d} {:f}|".format(name,age,average))
