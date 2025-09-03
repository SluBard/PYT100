def positives(lis):
    new = list()
    for elem in lis:
        if elem > 0:
            new.append(elem)
    return new

mylist = [ -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(positives(mylist))
