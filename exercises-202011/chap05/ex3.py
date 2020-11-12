def func():
    def sum(a,b):
        return a+b
    return sum

s = func()
print(s(2,3))
