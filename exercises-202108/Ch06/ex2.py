import myfuncs

def add(a,b):
    print("We are in local add")
    return a+b

print(myfuncs.add(1,2))
print(add(1,2))
