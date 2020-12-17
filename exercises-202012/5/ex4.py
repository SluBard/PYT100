def my():
    return lambda a,b:a+b

f = my()
print(f.__name__)
print(f(5,5))
        
