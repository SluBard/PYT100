first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))
if first > second:
    print("The first number was larger: {}".format(first))
elif second > first:
    print("The second number was larger: {}".format(second))
else:
    print("The numbers are equal")
