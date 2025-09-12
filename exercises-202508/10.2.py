import re
while True:
    line = input("Enter a decimal number: ")
    if line == "q":
        break
    x = re.search(r'^([+-]?)\d*.\d+$',line)
    if x.group(1) == "-":
        print("Negative")
    else:
        print("Positive")
    
