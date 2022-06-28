import re

while True:
    line = input("Enter Number: ")
    # nnXX Desc
    r=re.search('^(\d{2})([A-Z]{2})\s+(.+)$',line)
    if r:
        print(r.group(1))
        print(r.group(2))
        print(r.group(3))
