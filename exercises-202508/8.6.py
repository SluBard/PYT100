histogram=dict()
for i in range(1,5):
    fname="file"+str(i)
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

