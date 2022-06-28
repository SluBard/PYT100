import sys

list1 = ['file1','file2','file3','file4']

dict1 = dict()
for item in list1:
    f1 = open(item,"r")
    names = f1.readlines()
    for name in names:
        dict1[name] = dict1.get(name,0) + 1

list2 = list(dict1.keys())
list2.sort()

for name in list2:
    print("{:10}{:5}".format(name.replace('\n',''),dict1.get(name)))

    
