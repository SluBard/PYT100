import sys

hist = dict()

if len(sys.argv) <2:
    print("Usage: {} file1 ...".format(sys.argv[0]))
    exit(1)

sys.argv.pop(0)

for file in sys.argv:
    list1 = open(file,"r").readlines()
    for line in list1:
        key = line.strip()
        hist[key] = hist.get(key,0)+1


names = list(hist.keys())
names.sort()
for name in names:
    print("{}\t\t{}".format(name,hist[name]))


