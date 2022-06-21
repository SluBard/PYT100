numbers = input("Enter set of numbers: ").split()

print("Numbers entered greater than zero: ", end="")
for number in numbers:
    if float(number) > 0:
        print("{} ".format(number),end="")
        


    
