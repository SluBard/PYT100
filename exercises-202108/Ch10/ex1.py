import re

while True:
    line = input(">")
    x=re.search('([+-])?\d+',line)
    if x:
        if x.group(1) == None or x.group(1) == '+':
            print("The number is positive")
        else:
            print("The number is negative")
