#!/usr/bin/env python3
lis = [10, 20, 30, 40, 20, 50]
fmt = "%32s %s"
print(fmt % ("Original:", lis))

print(fmt % ("Pop Last Element:", lis.pop()))
print(fmt % ("Pop Element at pos# 2:", lis.pop(2)))
print(fmt % ("Resulting List:", lis))

lis.append(100)
print(fmt % ("Appended 100:", lis))
lis.remove(20)
print(fmt % ("Removed First 20:", lis))
lis.insert(1, 1000)
print(fmt % ("Inserted 1000 at pos# 1:", lis))

lis.sort()
print(fmt % ("Sorted:", lis))
lis.reverse()
print(fmt % ("Reversed:", lis))
