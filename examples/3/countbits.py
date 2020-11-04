#!/usr/bin/env python3
""" Count the bits that are set in a variable """

count  = 0
value = 213
print("Number")
print("    Dec:", value)
print("    Hex:", hex(value))
print("    Oct:", oct(value))
print("    Bin:", bin(value))
print()
while value > 0:
    result = value & 1
    fmt = "{0:08b} & {1:08b} =  {2}"
    txt = fmt.format(value, 1, result)
    print(txt)
    
    if value & 1:  # bitwise AND
        count += 1
    value = value >> 1 # bit shift right

print("# of set bits:", count)
