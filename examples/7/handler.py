#!/usr/bin/env python3
total = 0
while True:
	value = input("Please enter a number: ")
	if  value == "end":
		break
	try:
		total += int(value)
	except ValueError:
		print("Invalid number - try again")
		
print("Total is", total)         
