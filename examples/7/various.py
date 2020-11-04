#!/usr/bin/env python3
total = 0

# Custom Handler
try:
    value = input("Please enter a number: ")
    total += int(value)
except ValueError:
    print("Invalid number")
    exit(1)
print("Total is", total)

# Default System's Handler
value = input("Please enter a number: ")
total += int(value)
print("Total is", total)   

     
#Another Custom Handler
try:
    value = input("Please enter a number: ")
    total += int(value)
except ValueError:
    print("Invalid number")
    exit(2)
print("Total is", total)        
