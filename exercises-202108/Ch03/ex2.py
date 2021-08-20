i1 = input("Enter a number: ")
i2 = input("Enter a number: ")
i1 = int(i1)
i2 = int(i2)
total=0
for i in range(i1,i2+1):
    total += i
print("Sum of integers: {}".format(total))
