#!/usr/bin/env python3
def thesum(param):
	total = 0
	for elem in param:
		total += elem
	return total

data = [ 10, 20, 30, 40 ]
x = thesum(data)
print(x)

vals = [ ]
for i in range(10):
	vals.append(i)
x = thesum(vals)
print(x)
