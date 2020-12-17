def my(lis):
    new=list()
    for i in lis:
        if i>0:
            new.append(i)
    return new

list1=[-5,-3,-1,1,3,5]
list2=my(list1)
print(list2)

