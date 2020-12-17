sum=0
while True:
    try:
        data = input("Enter an integer: ")
        if data.lower() == "end":
            break
        value=int(data)
        sum += value
    except ValueError as err:
        print(err)
    except KeyboardInterrupt as err:
        print("Type 'end' to exit")
    except EOFError as err:
        break
print("Sum of numbers entered is: {}".format(sum))
