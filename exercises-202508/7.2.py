
lis = [0,1,2,3,4,5,6,7,8,9]
while True:
    val = input("Enter index from 0 to 9(end to end): ")
    if val == "end":
        break
    try:
        if int(val) < 0:
            raise IndexError("Negative numbers not allowed")

        print("Lookup with index: {} produced {}".format(val,lis[int(val)]))
        
    except (ValueError, IndexError) as err:
        print(err)
