myset=set()
while True:
    data = input("Enter a line:(q to quit) ")
    if data.lower() == "q":
        break
    for word in data.split():
        myset.add(word)

mylist = list(myset)
mylist.sort()
print(mylist)
print("Number of unique words is: {}".format(len(myset)))
    
