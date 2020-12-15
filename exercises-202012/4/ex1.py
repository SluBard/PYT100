myset=set()
count=0
while True:
    n1 = input("Enter a number:(end to quit) ")
    if n1.lower() == "end":
        break
    if n1 in myset:
        count+=1
    else:
        myset.add(n1)
        
print(myset)
print("Number not entered into the set",count)

