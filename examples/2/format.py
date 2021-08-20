#!/usr/bin/env python3
quot = "first name: {}\nlast name: {}"
line = quot.format("mike", "smith")
print(line)

firstname="Michael"
lastname="Smith"
quot="first name: {first}\nlast name: {last}"
line=quot.format(first=firstname, last=lastname)
print(line)

quot = "first name: {1}\nlast name: {0}"
line = quot.format("smith","mike" )
print(line)
