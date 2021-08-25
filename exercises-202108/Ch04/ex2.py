set1 = set()

while True:

    data = input("enter a line (q to quit) ")

    if data == "q":
        break

    words = data.split()
    set1 = set1 | set(words) # Union new words into set

list1 = list(set1)
list1.sort()
for i in list1:
    print("{} ".format(i),end="")
print()

print("Number of unique words: {}".format(len(set1)))
