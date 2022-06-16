#!/usr/bin/env python3
x = "10"
y = 20
result = int(x) + y + int("30")
print(result)
print("The result is: " + str(result))
print("The result is: ",result,end='',sep='')
print("The result is: {}".format(result))
a = 23.45
b = "12.34"
print(a + float(b))
print(ord("A"))
print(chr(65))



for x in range(10):
    print("{},".format(x),end='')
