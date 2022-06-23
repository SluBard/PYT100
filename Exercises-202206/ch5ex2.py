def clip(*arg, num=0):
    count = 0
    for i in arg:
        if i > num:
            count += 1
    return count

val = clip(5, -10, 10, -20, 30, num = 0)
print(val)
