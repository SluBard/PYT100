def offset(num,dict1):
    for i in dict1.keys():
        dict1[i] += num

d = {1:1,2:2,3:3,4:4}
d1= {1:[1,2]} # value is a list of two integers
offset(5, d)
print(d)
