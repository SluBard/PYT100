#!/usr/bin/env python3
import sys

f = open(sys.argv[1], 'w') 
f.write('This is a test.\n') 
f.write('This is another test.\n') 
f.close()
