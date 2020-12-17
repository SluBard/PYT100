def my(*args,num):
    total=0
    for i in args:
        if i > num:
            total += 1
    return total

result = my(5,-10,10,-20,30,num=0)
print(result)
        
