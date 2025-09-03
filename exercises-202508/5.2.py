def above(*args,base=0):
    count = 0
    for elem in args:
        if elem > base:
            count += 1
    return count

print( above(5, -10, 10, -20, 30, base = 0) )
