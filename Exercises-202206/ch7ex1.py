list1 = [0,1,2,3,4,5,6,7,8,9]

while True:
    input1 = input("Enter a number(end to exit): ")
    if input1 == "end":
        break
    try:
        index = int(input1)
        print("Value located at index location {} is {}".format(index,list1[index]))
    except ValueError:
        print("Please enter integers only.")
    except IndexError:
        print("Please enter a value from 0 to 9")
    
