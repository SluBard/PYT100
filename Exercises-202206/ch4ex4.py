def usethis(akey):
    return dict1[akey]
    
dict1 = dict()

while True:
    data = input("enter a line (q to quit) ")
    if data == 'q':
        break

    list1 = data.split()
    for word in list1:
        dict1[word] = dict1.get(word,0) + 1

keys = list(dict1.keys())

print("Sorted by key")
keys.sort()
for key in keys:
    print("{} - {}".format(key,dict1[key]))

print("Sorted by value")    
keys.sort(key=usethis)
for key in keys:
    print("{} - {}".format(key,dict1[key]))
