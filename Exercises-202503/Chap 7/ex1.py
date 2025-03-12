lis=[0,1,2,3,4,5,6,7,8,9]
while True:
    data = input("input numerical index (end to exit)")
    if data == 'end':
        break
    try:
        value = lis[int(data)]

    except (ValueError,IndexError):
        print("Enter a valid index 0-9")
    else:
        print("item at index {} has a value of {}".format(data,value))
