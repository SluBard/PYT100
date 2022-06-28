import re

while True:
    line = input("Enter Number: ")
    r=re.search('^([+-])?\d*\.\d+$',line)
    #x=re.search('^([+-])?\d+\.\d+$',line)
    #x=re.search('^([+-])?\d{1,}\.\d{1,}$',line)
    if r:
        if r.group(1) == None or r.group(1) == '+':
            print("The number is positive")
        else:
            print("The number is negative")
