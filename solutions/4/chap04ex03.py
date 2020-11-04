#!/usr/bin/env python3
#
# A Solution For Chapter 4 Exercise 3
#
themap = { 0:'zero', 1:'one', 2:'two', 3:'three', 4:'four',
           5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

value = input("Enter a number: ")

for i in value:
    print(themap[int(i)], end=" ")

print()
