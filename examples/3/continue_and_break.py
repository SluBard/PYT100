#!/usr/bin/env python3
cnt = 0
total = 0
while cnt <= 100:
    cnt += 1
    if cnt % 4 == 0:
        continue         # skip even multiples of 4
    if cnt * cnt >  400:
        break            # will happen at cnt = 21
    total += cnt
else:
    print("Might not get here")
print("Total is:", total)
print("Count is:", cnt)

