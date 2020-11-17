list1 = []
for i in range(10):
    list1.append(i)

while True:
    data1 = input("Enter index (end to exit): ")
    if data1 == "end":
        break
    try:
        index = int(data1)
    except:
        print("illegal number: try again")
        continue
    try:
        print("Value at index {} is {}".format(index,list1[index]))
    except:
        print("Bad index")
        

