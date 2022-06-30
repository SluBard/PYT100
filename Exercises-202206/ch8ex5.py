import sys

if len(sys.argv) != 3:
    print("Usage: {} file1 file2".format(sys.argv[0].split('\\')[-1]))
    exit()

f1 = open(sys.argv[1],"r")
f2 = open(sys.argv[2],"r")

s1 = set(f1.readlines())
s2 = set(f2.readlines())

list1 = list(s1 & s2)

print("Items common to files {} and {}".format(sys.argv[1],sys.argv[2]))
for item in list1:
    print("\t{}".format(item),end="")

    
