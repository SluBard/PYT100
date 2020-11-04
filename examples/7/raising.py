#!/usr/bin/env python3
result = input("enter an even number: ");
try:
    pos = int(result)
    if int(pos) % 2 != 0:
        raise ValueError("# Not Even:" + str(pos))
    print("Number is", pos)
except ValueError as err:
    print(err)
