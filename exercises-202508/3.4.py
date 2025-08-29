string = input("Enter lower, upper, step: ")

lower = int(string.split(',')[0])
upper = int(string.split(',')[1])
step = int(string.split(',')[2])
for i in range(lower,upper,step):
    print(i,end=' ')
print()
    
numbers = string.split(',')
for i in range(int(numbers[0]),int(numbers[1]),int(numbers[2])):
    print(i,end=' ')
print()    


lower,upper,step = (int(i) for i in string.split(','))
for i in range(lower,upper,step):
    print(i,end=' ')
print()

thing=(int(i) for i in string.split(','))
for i in range(*thing):
    print(i,end=' ')
print()  

for i in range(*(int(i) for i in string.split(','))):
    print(i,end=' ')
print()  
