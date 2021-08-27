def outer():
    return lambda a,b:a+b

sum = outer()

print(sum(1,2))
