def fun():
    def morefun(a,b):
        return a+b

    return morefun

f=fun()
print(f.__name__)
print(f(3,4))
print(fun()(3,4))
