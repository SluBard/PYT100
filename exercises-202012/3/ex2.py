n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
sum=0
for i in range(n1,n2+1):
    sum+=i # sum = sum + i
print("Sum of range from {} to {} is {}".format(n1,n2,sum))
