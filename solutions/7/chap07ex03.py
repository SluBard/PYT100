#!/usr/bin/env python3
#
# A Solution For Chapter 7 Exercise 3
#
total = 0
while True:
    try:
        line = input("> ")
        total = total + int(line)
        print("added: " + line)	
    except EOFError:
        print("caught it")
        break
    except ValueError:
        print("Must input a number")
        continue
    except KeyboardInterrupt:
        print("Use Ctrl-D (Linux) or Ctrl-Z (Windows) to terminate")
	
print("SUM IS", total)
