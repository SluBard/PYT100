def sort(lis):
    return sorted(lis)

def reverse(lis):
    return sorted(lis, reverse=True)

values = [ 10, 40, 30, 20, 5 ]
print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
print(values)
