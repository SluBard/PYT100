#!/usr/bin/env python3
total = 0
while True:
    value = input("Please enter a number: ")
    if  value == "end":
        break
    total += int(value)

print("Total is", total) 
