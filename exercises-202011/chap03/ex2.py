data1 = input("Enter first number: ")
data2 = input("Enter second number: ")
num1 = int(data1)
num2 = int(data2)
sum = 0
for i in range(num1, num2+1):
    sum += i
print("Sum is: {}".format(sum))
