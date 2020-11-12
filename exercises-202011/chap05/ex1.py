def positives(lis):
    newlis = list()
    for item in lis:
        if item > 0:
            newlis.append(item)
    return newlis

l1 = [-2, -1, 0, 1, 2]
print(positives(l1))
