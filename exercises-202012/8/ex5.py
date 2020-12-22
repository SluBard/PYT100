import sys

if len(sys.argv) !=3:
    print("Usage: {} file1  file2".format(sys.argv[0]))
    exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]

list1 = open(file1,"r").readlines()
list2 = open(file2,"r").readlines()

set1 = set(list1)
set2 = set(list2)

print(list(set1&set2))

