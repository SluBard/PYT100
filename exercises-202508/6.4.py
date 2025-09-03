import sys
sum=0
for i in sys.argv[1:]:
    sum += int(i)
print("Sum is {}".format(sum))
