words = set()
while True:
    data = input("enter a line (q to quit): ")
    if data == 'q':
        break
    linewords = data.split()
    for word in linewords:
        words.add(word)


print("Sorted Unique words: {}".format(sorted(words)))
print("Count of unique words: {}".format(len(words)))
