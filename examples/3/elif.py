#!/usr/bin/env python3
x = 0
if x <= 5:
	print("x le 5")
elif x <= 10:
	print("x between 5 and 10")
elif x <= 15:
	print("x between 10 and 15")
else:
	print("x gt 15")
print("done with the elif tests")

x = 5
if x == 5:
        y=2
else:
        y=3

#ternery expression example
y = 2 if x == 5 else 3
print(x,y)
