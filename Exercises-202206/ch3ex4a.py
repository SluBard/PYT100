mylist = input("Enter lower/upper/step values: ").split()
lower = int(mylist[0])
upper = int(mylist[1])
step = int(mylist[2])

for i in range(lower,upper,step):
    print("{} ".format(i),end="")
        


    
