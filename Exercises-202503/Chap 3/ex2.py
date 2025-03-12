i1 = int(input("enter 1st integer "))
i2 = int(input("enter 2nd integer "))
sum=0
for x in range(i1,i2+1):
    sum += x
print("Sum of numbers from {} to {} is {}".format(i1,i2,sum))
