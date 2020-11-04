#!/usr/bin/env python3
f = open('test.txt', 'a')
f.write('Appended to the bottom')
f.write(' of the file\n')
f.write('More at the bottom\n')
f.close()
