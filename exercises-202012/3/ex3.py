numbers = input("Enter a series of numbers: ")

print("These are the numbers greater than zero")
list1=numbers.split()
for i in list1:
    if int(i) > 0:
        print(i,end=" ")
print()
