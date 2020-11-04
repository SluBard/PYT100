#!/usr/bin/env python3
import time

now = time.time()    # time as seconds since epoch
print("Seconds since epoch (1/1/1970):", now)

date = time.ctime(now)# time as the date
print("Date as a string is:", date)

pieces = time.localtime()    # grab pieces of time
print(type(pieces))
for piece in pieces:    # print each piece
    print(piece)

print(time.strftime("YR/MO/DY is %Y/%m/%d"))
