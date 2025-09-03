def common( lis1, lis2):
    return list(set(lis1)&set(lis2))

mylis1 = [1,2,3,4,5]
mylis2 = [4,5,6,7,8]

print(common(mylis1,mylis2))
