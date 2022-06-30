import sys

if len(sys.argv) < 3:
    print("Usage: {} file1 file2 [filen...]".format(sys.argv[0].split('\\')[-1]))
    exit()

#list1 = ['file1','file2','file3','file4']
list1 = sys.argv[1:]

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

    
