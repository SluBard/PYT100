def sort(lis):
    copy = list(lis)
    copy.sort()
    return copy

def reverse(lis):
    copy = list(lis)
    copy.reverse()
    return copy

values=[10,40,30,20,5]
print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
