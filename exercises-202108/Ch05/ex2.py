def pos(*var,num):
    count=0
    for i in var:
        if i > num:
            count += 1
    return count

result = pos(5,-10,10,-20,30,num=0)
print(result)
        
    
