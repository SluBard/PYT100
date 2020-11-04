#!/usr/bin/env python3
#
# A Solution For Chapter 4 Exercise 2
#
words =  set()

while True:
    data = input("enter a line (q to quit): ")
    if data == 'q':
        break
	
    linewords = data.split()
    for word in linewords:
        words.add(word)
	
thelist = list(words)
thelist.sort()

for i in thelist:
    print(i)

print(len(thelist), "words in all")
