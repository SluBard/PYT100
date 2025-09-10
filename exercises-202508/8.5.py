import sys
if len(sys.argv) != 3:
    print("Usage:\npython3 {} file1 file2".format(sys.argv[0]))
    exit()
    
infile = sys.argv[1]
otfile = sys.argv[2]
f1 = open(infile,"r")
f2 = open(otfile,"r")

common=list(set(f1.readlines())&set(f2.readlines()))

f1.close()
f2.close()

for name in common:
    print(name,end="")

