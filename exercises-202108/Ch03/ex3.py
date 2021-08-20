s1 = input("Enter a list of numbers: ")
list=s1.split()
for element in list:
    if int(element) > 0:
        print("{} ".format(element),end='')
print()
