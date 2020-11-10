while True:
    data = input("enter a line (q to quit): ")
    if data == 'q':
        break
    word_list = data.split()
    unique_words = set(word_list)
    print("Found ",len(unique_words)," unique words")
    print( sorted(unique_words) )
