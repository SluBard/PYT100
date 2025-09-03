#!/usr/bin/env python3
def multiple_of_three(x): 
    return x % 3 == 0

results = filter(multiple_of_three, range(2, 51))
for value in results:
    print(value, end=' ')
print()

print(type(results))
print(list(filter(multiple_of_three, range(2, 51))))
