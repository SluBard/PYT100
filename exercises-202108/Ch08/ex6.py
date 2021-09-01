import sys

if len(sys.argv) <= 1:
    print("Usage:",sys.argv[0].split('\\')[-1],"file1 ... filen")
    exit(0)

mydict = dict()
for file in sys.argv[1:]:
    tfile = open(file,"r")
    lines = tfile.readlines()
    for line in lines:
        key = line.strip()
        mydict[key] = mydict.get(key,0)+1
    tfile.close()

names = list(mydict.keys())
names.sort()
for name in names:
    print("{}\t\t{}".format(name,mydict[name]))
