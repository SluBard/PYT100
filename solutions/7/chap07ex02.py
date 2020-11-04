#!/usr/bin/env python3
#
# A Solution For Chapter 7 Exercise 2
#
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    result = input("enter a number: ");
    if result == "end":
        break;

    try:
        pos = int(result)
        if ( pos < 0 ):
            raise IndexError("Attempt to use negative index:" + str(pos))
        print(array[pos])
	
    except ValueError:
        print("result is not an integer")
    except IndexError:
        print("index out of range")
