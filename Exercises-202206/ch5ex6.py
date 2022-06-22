def common(lis1, lis2):
    s1=set(lis1)
    s2=set(lis2)
    return list(s1 & s2)


values1 = [10,40,20,5]
values2 = [40,30,20,5]


print(common(values1,values2))
