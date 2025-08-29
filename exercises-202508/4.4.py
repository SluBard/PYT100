def sortbycounts(key):
    return words.get(key)
    
words = dict()
while True:
    data = input("enter a line (q to quit): ")
    if data == 'q':
        break
    linewords = data.split()
    for word in linewords:
        words[word]= words.get(word,0) + 1

mylist = list(words.keys())
mylist.sort()
print("Sorted Unique words: {}".format(mylist))
mylist.sort(key=sortbycounts)
print("Sorted by Count: {}".format(mylist))

print("Sorted Unique words: {}".format(sorted(mylist)))
print("Sorted by Count: {}".format(sorted(mylist,key=sortbycounts)))
