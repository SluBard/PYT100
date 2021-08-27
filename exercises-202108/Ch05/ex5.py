
def sort(l):
    new=list(l)
    new.sort()
    return new

def reverse(l):
    new=list(l)
    new.reverse()
    return new

values = [10,40,30,20,5]

print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
print(values)
