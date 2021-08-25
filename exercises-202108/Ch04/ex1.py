set1 = set()
count=0

while True:

    s1 = input("Enter a number: ")

    if s1 == "end":
        break

    if s1 in set1:
        print("{} is already in the set.".format(s1))
        count+=1
        continue

    set1.add(s1)

print(set1)
print("{} entries not added to set.".format(count))
