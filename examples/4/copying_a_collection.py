#!/usr/bin/env python3
list1 = [ 1, 2, 3 ]
list2 = list(list1)
print("Lists: ", id(list1), ":", id(list2))

tuple1 = (4, 5, 6)
tuple2 = tuple(tuple1)
print("Tuples: ", id(tuple1), ":", id(tuple2))

set1 = {7, 8, 9}
set2 = set(set1)
print("Sets: ", id(set1), ":", id(set2))

dict1 = {"A":10, "B":11, "C":12}
dict2 = dict(dict1)
print("Dictionaries: ", id(dict1), ":", id(dict2))
