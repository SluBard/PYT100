def positive(lis):
    new= list()
    for i in lis:
        if i > 0:
            new.append(i)
    return new

lis1 = [ -3, -2, -1, 0, 1, 2, 3 ]
lis2 = positive(lis1)
print(lis2)
