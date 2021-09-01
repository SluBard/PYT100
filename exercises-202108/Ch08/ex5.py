import sys

try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
except:
    print("Usage:",sys.argv[0].split('\\')[-1],"file1 file2")
    exit(0)

inf1 = open(file1,"r")
inf2 = open(file2,"r")


list1 = inf1.readlines()
list2 = inf2.readlines()

list3 = set(list1) & set(list2)

for item in list3:
    print(item,end="")
