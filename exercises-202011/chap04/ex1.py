set1 = set()
not_added = 0
while True:
    s1 = input("Enter a number: ")
    if s1.lower() == "end":
        break
    if int(s1) in set1:
        not_added +=1
    else:
        set1.add(int(s1))
print("set: ",set1)
print(not_added, " not added to set")
