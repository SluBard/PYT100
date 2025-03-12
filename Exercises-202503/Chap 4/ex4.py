def usethis(akey):
    return d1[akey]
    
d1 = dict()

while True:
    data = input("enter a line (q to quit) ")
    if data == 'q':
        break

    l1 = data.split()
    for word in l1:
        d1[word] = d1.get(word,0) + 1

keys = list(d1.keys())

print("Sorted by key")
keys.sort()
for key in keys:
    print("{} - {}".format(key,d1[key]))

print("Sorted by value")    
keys.sort(key=usethis)
for key in keys:
    print("{} - {}".format(key,d1[key]))
