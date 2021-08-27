def common(list1,list2):
    s1 = set(list1)
    s2 = set(list2)
    return list(s1&s2)

l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]

print(common(l1,l2))
    
