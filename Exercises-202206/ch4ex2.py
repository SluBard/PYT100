set1 = set()

while True:
    data = input("enter a line (q to quit) ")
    if data == 'q':
        break

    list1 = data.split()
    for word in list1:
        set1.add(word)

print("Number of unique words: {}".format(len(set1)))
print("Sorted unique words: {}".format(sorted(set1)))
