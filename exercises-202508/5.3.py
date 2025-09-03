def outer():
    def inner( a, b):
        return a*b
    return inner

y=outer()
print(y( 6, 6))
