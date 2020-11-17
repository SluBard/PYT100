map=dict()
for i in range(4):
    f = open('file'+str(i+1),'r')
    for j in f:
        key=j.strip()
        map[key]=map.get(key,0)+1

l1 = list(map.keys())
l1.sort()
for i in l1:
    print("{}\t{}".format(i,map.get(i)))
    
