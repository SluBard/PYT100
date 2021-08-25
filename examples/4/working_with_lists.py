#!/usr/bin/env python3
lis = [10, 20, 30, 40, 20, 50]
#fmt = "%32s %s" <--- old way
fmt = "{:32s} {}" #<--- new way
#print(fmt % ("Original:", lis))
print(fmt.format("Original:", lis))

#print(fmt % ("Pop Last Element:", lis.pop()))
#print(fmt % ("Pop Element at pos# 2:", lis.pop(2)))
#print(fmt % ("Resulting List:", lis))
print(fmt.format("Pop Last Element:", lis.pop()))
print(fmt.format("Pop Element at pos# 2:", lis.pop(2)))
print(fmt.format("Resulting List:", lis))

lis.append(100)
#print(fmt % ("Appended 100:", lis))
print(fmt.format("Appended 100:", lis))
lis.remove(20)
#print(fmt % ("Removed First 20:", lis))
print(fmt.format("Removed First 20:", lis))
lis.insert(1, 1000)
#print(fmt % ("Inserted 1000 at pos# 1:", lis))
print(fmt.format("Inserted 1000 at pos# 1:", lis))

lis.sort()
#print(fmt % ("Sorted:", lis))
print(fmt.format("Sorted:", lis))
lis.reverse()
#print(fmt % ("Reversed:", lis))
print(fmt.format("Reversed:", lis))

