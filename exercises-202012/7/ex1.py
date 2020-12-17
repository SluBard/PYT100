mylist=[0,1,2,3,4,5,6,7,8,9]

while True:
    data = input("Enter an integer: ")
    if data.lower() == "end":
        break
    try:
        index=int(data)
        value=mylist[index]
        print("Value at index position {} is {}".format(index,value))
    except ValueError as err:
        print(err)
    except IndexError as err:
        print(err)
        
