#!/usr/bin/env python3
txt1 = "This,is,a,comma,separated,string"
txt2 = "This    is whitespace\t\tseparated"
pieces = txt1.split(",")
print(pieces,pieces[0])
for piece in pieces:
    print(piece)
print()

pieces = txt2.split()
for piece in pieces:
    print(piece)


for i in range(len(pieces)):
    print(i,pieces[i])

for i in pieces:
    print(i)
