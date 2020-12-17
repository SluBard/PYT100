from ex1 import *
#import ex1

def add(a,b):
    print("local add")
    return a+b
def mul(a,b):
    print("local mul")
    return a*b

print(add(1,2))
print(mul(2,3))
print(add(1,2))
print(mul(2,3))
#print(ex1.add(1,2))
#print(ex1.mul(2,3))
