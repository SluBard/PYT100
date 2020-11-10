data1 = input("Enter a series of numbers on one line: ")
for i in data1.split():
    if float(i)>0:
        print(i)
