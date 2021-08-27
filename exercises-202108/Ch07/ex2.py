list1 = [0,1,2,3,4,5,6,7,8,9]

while True:
    s1 = input("Enter a number ('end' to end): ")
    if s1 == 'end':
        break
    try:
        num = int(s1)
        if num < 0:
            raise IndexError("Enter a positive number")
        print("Found {} at index {}".format(list1[num],num))
    except IndexError as e:
        print("IndexError",e)
    except ValueError as e:
        print("ValueErorr",e)
