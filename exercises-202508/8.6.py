import sys
if len(sys.argv) < 2:
    print("Usage:\npython3 {} file1 ... filen".format(sys.argv[0]))
    exit()
    
sys.argv.pop(0)

histogram=dict()
for fname in sys.argv:
    f=open(fname)
    names = f.readlines()
    for name in names:
        nm=name.strip()
        histogram[nm] = histogram.get(nm,0) + 1
    f.close()
    
lis = list(histogram.keys())
lis.sort()
for name in lis:
    print("{}\t{}".format(name,histogram[name]))

