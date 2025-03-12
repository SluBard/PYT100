not_added=0
s=set()

while True:
    val = input("Enter a number (end to quit): ")
    if val.lower() == 'end':
        break
    if val in s:
        not_added += 1
    else:
        s.add(val)

print(s)
print("count of numbers not added {}".format(not_added))
