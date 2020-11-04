#!/usr/bin/env python3
import os
# Reading from file in binary mode
file = open("seekdata.txt", "rb")
print(file.read())

file.seek(3, os.SEEK_SET)
print(file.read(5))
print("Position:", file.tell())

file.seek(12, os.SEEK_CUR)
print(file.read(7))
print("Position:", file.tell())

file.seek(-20, os.SEEK_CUR)
print(file.read(5))
print("Position:", file.tell())
file.close()

print("#" * 30)

# Reading from file in text mode
file = open("seekdata.txt", "r")
print(file.read())

file.seek(12, os.SEEK_SET)
print(file.read(5))
print("Position:", file.tell())

file.seek(0, os.SEEK_CUR)
print(file.read(7))
print("Position:", file.tell())

file.seek(0, os.SEEK_CUR)
print(file.read(5))
print("Position:", file.tell())
file.close()
