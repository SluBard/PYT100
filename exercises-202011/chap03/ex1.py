data1 = input("Enter first number: ")
data2 = input("Enter second number: ")
num1 = float(data1)
num2 = float(data2)
if num1>num2:
    print("{} is bigger than {}".format(num1,num2))
elif num2>num1:
    print("{1} is bigger than {0}".format(num1,num2))
else:
    print("{} is equal to {}".format(num1,num2))
