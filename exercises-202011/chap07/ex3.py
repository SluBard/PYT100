list1=list()
while True:
    data = input("Enter an integer: ")
    try:
        value = int(data)
        list1.append(value)
    except ValueError as e:
        print("ValueError: {}".format(e))
        continue
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt")
        continue
    except EOFError as e:
        print("EOFError")
        break
sum=0
for i in list1:
    sum += i

print("Sum is: {}".format(sum))

