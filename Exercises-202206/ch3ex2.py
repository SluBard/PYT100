integer1 = int(input("Enter first integer: "))
integer2 = int(input("Enter second integer: "))

total = 0
for i in range(integer1, integer2):
    print("{} + ".format(i),end='')
    total += i

total += i+1
print("{} = {}".format(i+1,total))


    
