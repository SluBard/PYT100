#!/usr/bin/env python3
x = 10;
y = 20;
data = (x, y, 5, 30, 7) # creating a tuple
print("tuple contents:", data)
print("a slice:", data[2:4])

# converting tuple to list
as_list = list(data)
as_list.sort()
print("List:", as_list)

# converting list to tuple
data = tuple(as_list)
print("tuple contents", data)
