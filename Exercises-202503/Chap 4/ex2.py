s1 = set()
while True:
    data = input("enter a line (q to quit) ")
    if data == 'q':
        break
    l1 = data.split()
    for w in l1:
        s1.add(w)

print("Number of unique words: {}".format(len(s1)))
print("Sorted unique words: {}".format(sorted(s1)))
