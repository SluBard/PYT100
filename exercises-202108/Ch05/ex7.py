def mymap(num,dict1):
    for key,value in dict1.items():
        dict1[key]+=num

dict1 = {1:10,2:20,3:30,4:40}
mymap(10,dict1)
print(dict1)
