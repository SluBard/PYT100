set1 = set()
list1 = list()
while True:
    inp = input("Input a number ('end' to exit): ")
    if inp.lower() == 'end':
        break
    if inp in set1:
        list1.append(inp)
    else:
        set1.add(inp)
        
print("Set: {}".format(set1))
print("Not added to set: {}".format(list1))
print("Number of items not added to set: {}".format(len(list1)))


    
