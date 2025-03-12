def common(l1, l2):
    s1=set(l1)
    s2=set(l2)
    return list(s1&s2)

lis1=[1,2,3,4,5]
lis2=[4,5,6,7,8]

print(common(lis1,lis2))
