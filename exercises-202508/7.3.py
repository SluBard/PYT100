total=0
while True:
    try:
        val = int(input("Enter numbers: "))
        total += val
    except ValueError as err:
        print(err)
    except KeyboardInterrupt as err:
        print("CTL-C caught")
    except EOFError as err:
        break;
print("Total = {}".format(total))
