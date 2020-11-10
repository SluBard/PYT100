def byvalue(key):
    return unique_words.get(key)


while True:
    unique_words = dict()
    data = input("enter a line (q to quit): ")
    if data == 'q':
        break
    for word in data.split():
        value = unique_words.get(word,0) + 1
        unique_words[word] = value
    print("Found ",len(unique_words)," unique words")
    print("Sorted by words:")
    for word in sorted(unique_words.keys()):
        print(word)

    print("Sorted by word frequency:")
    for word in sorted(unique_words.keys(),key=byvalue):
        print(word,':',unique_words.get(word))

