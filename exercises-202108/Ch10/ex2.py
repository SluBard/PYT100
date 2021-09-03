import re

while True:
    line = input(">")
    x=re.search('^([+-])?\d*\.\d+$',line)
    #x=re.search('^([+-])?\d+\.\d+$',line)
    #x=re.search('^([+-])?\d{1,}\.\d{1,}$',line)
    if x:
        if x.group(1) == None or x.group(1) == '+':
            print("The number is positive")
        else:
            print("The number is negative")
