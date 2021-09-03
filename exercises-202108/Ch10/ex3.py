import re

while True:
    line = input(">")
    # nnXX Desc
    x=re.search('^(\d{2})([A-Z]{2})\s+(.+)$',line)
    if x:
        print(x.group(1))
        print(x.group(2))
        print(x.group(3))
