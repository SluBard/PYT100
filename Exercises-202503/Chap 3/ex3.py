s1 = input("input a list of numbers separated by spaces ")
for v in s1.split():
    if int(v) > 0:
        print(v,end=' ')
        
