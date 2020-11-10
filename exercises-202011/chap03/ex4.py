data1 = input("Enter lower limit: ")
data2 = input("Enter upper limit: ")
data3 = input("Enter step: ")
num1=int(data1)
num2=int(data2)
num3=int(data3)
for i in range(num1,num2,num3):
    print(i,end=" ")
print()
