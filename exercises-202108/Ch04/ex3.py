map1 = { 0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
         8:'eight',9:'nine' }

s1 = input("Enter a number: ")

for i in s1:
    print("{} ".format(map1[int(i)]), end="")
print()
