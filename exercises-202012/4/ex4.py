def usethis(akey):
    return mydict[akey]

mydict=dict()
while True:
    data = input("Enter a line:(q to quit) ")
    if data.lower() == "q":
        break
    for word in data.split():
        mydict[word]=mydict.get(word,0) + 1

mylist = list(mydict)
mylist.sort()
print("Sorted by key")
for item in mylist:
    print(item,mydict[item])

print("Sorted by count")
mylist.sort(key=usethis)
for item in mylist:
    print(item,mydict[item])
      
