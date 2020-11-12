def common(lis1, lis2):
    s1 = set(lis1)
    s2 = set(lis2)
    l1 = list(s1&s2)
    return l1

l1 = [ 10, 20, 30, 40, 50 ]
l2 = [ 30, 40, 50, 60, 70 ]

print(common(l1,l2))
