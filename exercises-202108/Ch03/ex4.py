lo = input("Enter lower limit: ")
hi = input("Enter higher limit: ")
step = input("Enter step: ")
for i in range(int(lo),int(hi),int(step)):
    print("{} ".format(i),end="")
print()
