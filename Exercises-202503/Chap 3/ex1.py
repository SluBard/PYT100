i1 = int(input("enter 1st integer "))
i2 = int(input("enter 2nd integer "))
if i1>i2:
    print("{} is larger than {}".format(i1,i2))
elif i2>i1:
    print("{} is larger than {}".format(i2,i1))
else:
    print("{} and {} are equal".format(i1,i2))
