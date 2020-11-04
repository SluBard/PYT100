#!/usr/bin/env python3
import time
date = time.ctime()
print("Date is:", date)

pieces = time.localtime()
print("Year:", pieces[0], "or", pieces.tm_year)
print("Month:", pieces[1], "or", pieces.tm_mon)
print("Day:", pieces[2], "or", pieces.tm_mday)
