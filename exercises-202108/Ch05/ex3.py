def outer():
    def inner(a,b):
        return a+b
    return inner

sum = outer()

print(sum(1,2))
