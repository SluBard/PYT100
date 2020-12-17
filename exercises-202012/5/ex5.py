def reverse(lis):
    new = list(lis)
    new.reverse()
    return new

def sort(lis):
    new = list(lis)
    new.sort()
    return new

list1 = [1,3,2,5,4,7,6,9,8]
print(sort(list1))
print(reverse(list1))
print(reverse(sort(list1)))
print(list1)
