#!/usr/bin/env python3
#
# A Solution For Chapter 4 Exercise 4
#
words = {}

while True:
    data = input("enter a line (q to quit): ")
    if data == 'q':
        break

    wordlist = data.split()
    for word in wordlist:
        words[word] = words.get(word, 0) + 1

keylist = list(words.keys())

print()
print("Words and Word count sorted by Words (the key)")
keylist.sort()
for eachkey in keylist:
    print(eachkey, words[eachkey])

print("Words and Word count sorted by Word Count (the Value)")
def customsorter(v):
    return words[v]

keylist.sort(key=customsorter)
for eachkey in keylist:
    print(eachkey, words[eachkey])
