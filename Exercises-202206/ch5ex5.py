def sort(lis):
    new=list(lis)
    new.sort()
    return new
    
def reverse(lis):
    new=list(lis)
    new.reverse()
    return new


values = [10,40,30,20,5]
print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
print(values)
