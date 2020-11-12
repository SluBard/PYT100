def plus( num, dict1):
    for key in dict1.keys():
        dict1[key] += num

d1 = { 1:2, 3:4, 5:6, 6:7 }
print(d1)
plus(1,d1)
print(d1)
        
