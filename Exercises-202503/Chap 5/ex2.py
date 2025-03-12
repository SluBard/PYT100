def fun(*arg,num):
    count = 0
    for element in arg:
        if element > num:
            count += 1
    return count

print(fun(5,-10,10,-20,30,num=0))
