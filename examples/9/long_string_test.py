#!/usr/bin/env python3
from long_string_error import LongStringError
max_length = 10

def checkstring(s):
    length = len(s)
    if length > max_length: 
        raise LongStringError("Line too long",
                                  length)

while True:
    try:
        line = input("Enter a line: ")
        checkstring(line)
        print("line is OK")
    except LongStringError as e:
        print(e, e.length())
