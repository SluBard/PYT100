import sys

sys.argv.pop(0)

sum=0
for i in sys.argv:
    sum += int(i)

print("sum of arguments: {}".format(sum))
    
