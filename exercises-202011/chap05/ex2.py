def greaterthan(*arg,num):
    count=0
    for item in arg:
        if item > num:
            count += 1
    return count

print(greaterthan(5,-10,10,-20,30,num=0))
