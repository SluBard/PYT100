def positives(l):
    new=list()
    for i in l:
        if i>=0:
            new.append(i)
    return new

list1 = [-3,-2,-1,0,1,2,3]
print(positives(list1))
