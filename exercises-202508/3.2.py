first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))

total=0
for i in range(first,second+1):
    total += i
    print("{} ".format(i),end='+ ')
print("= {}".format(total))

