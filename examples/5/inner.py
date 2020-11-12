#!/usr/bin/env python3
def outer(a, b):
    x = 15
    y = 20

    return lambda : print(a,b,x,y)
    #def inner():
    #    print(a, b, x, y)
    

    #return inner # reference to inner funtion

y = outer(5, 10)
print(type(y))
print(y.__name__)
y() # call the returned function
