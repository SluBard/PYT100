def usethis(key):
    return dict1[key]

dict1=dict()

while True:

    data = input("enter a line (q to quit) ")

    if data == "q":
        break

    words = data.split()
    for word in words:
        dict1[word] = dict1.get(word,0) + 1 

list1 = list(dict1)
list1.sort()
for i in list1:
    print("{} ".format(i),end="")
print()

list1.sort(key=usethis)
for i in list1:
    print("{}={} ".format(i,dict1[i]),end="")
print()
