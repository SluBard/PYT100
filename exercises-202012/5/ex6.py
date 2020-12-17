def union(a,b):
    s1=set(a)
    s2=set(b)
    return list(s1 & s2)

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
list3 = union(list1,list2)
print(list3)
