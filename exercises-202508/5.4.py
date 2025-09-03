def outer():
    return lambda a,b:a*b

y=outer()
print(y( 6, 6))
