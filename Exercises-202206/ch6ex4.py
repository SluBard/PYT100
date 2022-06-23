import sys

lis=sys.argv[1:]
total=0
for i in lis:
    total += int(i)
print("Sum of arguments: {}".format(total))
    
