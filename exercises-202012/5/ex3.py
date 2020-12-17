def my():
    def sum(a,b):
        return a+b
    return sum

f = my()
print(f.__name__)
print(f(5,5))
        
