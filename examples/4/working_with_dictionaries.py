#!/usr/bin/env python3
data = {'mike': 15, 'susan': 19, 'chris': 21}
while True:	
    key = input("Please enter a key: ")
    value = data.get(key, 0)
    if key.lower() == "quit":
        break
    if value:
        print("Value for ", key, "=", value)
    else:
        print(key, "is not present")
