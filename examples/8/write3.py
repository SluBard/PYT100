#!/usr/bin/env python3
filename = input("Enter file name: ")
f = open(filename, 'w') 
f.write('This is a test.\n') 
f.write('This is another test.\n') 
f.close()
