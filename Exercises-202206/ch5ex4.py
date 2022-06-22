def fun():
    return lambda a,b:a+b

f=fun()
print(f(3,4))
#print(fun()(3,4))
