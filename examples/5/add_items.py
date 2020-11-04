#!/usr/bin/env python3
def addvals(val, **items):
	total = 0
	for amt in items.values():
		if amt > val:
			total += amt
	return total

total = addvals(0, mike=100, jane=200, peter=300)
print(total)
