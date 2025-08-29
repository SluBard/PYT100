string = input("Enter a list of numbers: ")
for element in string.split():
    if int(element) > 0:
        print(element,end=' ')
