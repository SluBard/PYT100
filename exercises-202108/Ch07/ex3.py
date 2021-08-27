total = 0
while True:
    s1 = input("Enter a number ('end' to end): ")
    if s1 == 'end':
        break
    try:
        total += int(s1)
        print("Running total is {}".format(total))
    except ValueError as e:
        print("ValueErorr",e)
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt",e)
    except EOFError as e:
        print("EOFError",e)

