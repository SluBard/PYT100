f1 = open("file1","r")
f2 = open("file2","r")

common=list(set(f1.readlines())&set(f2.readlines()))
for name in common:
    print(name,end="")

f1.close()
f2.close()
