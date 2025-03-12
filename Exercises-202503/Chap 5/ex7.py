def bias(dict1, num):
    for element in dict1.keys():
        dict1[element]+=num

d={ 1:10, 2:20, 3:30, 4:40 }
print(d)
bias(d,10)
print(d)
