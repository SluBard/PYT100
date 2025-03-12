def sort(lis):
    l=list(lis)
    l.sort()
    return l

def reverse(lis):
    l=list(lis)
    l.reverse()
    return l

values=[10,40,30,20,5]
print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
print(values)
