import re
while True:
    line = input("Enter a part number and description: ")
    if line == "q":
        break
    x = re.search(r'^(\d{2})([A-Z]{2})\s+(.+)$',line)
    if not x:
        print("Invalid format, try again")
        continue
    print(x.group(1))
    print(x.group(2))
    print(x.group(3))

    
