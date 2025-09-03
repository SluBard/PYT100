def bias( mydict, bias ):
    for key in mydict.keys():
        mydict[key] += bias

mydictionary = { 1:1, 2:2, 3:3, 4:4, 5:5 }
print(mydictionary)
bias(mydictionary, 5)
print(mydictionary)
