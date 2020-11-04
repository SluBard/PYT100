#!/usr/bin/env python3
def power(base, expo):
    """ raises the base to expo power """
    answer = 1
    while expo > 0:
        answer *= base
        expo -= 1
    return answer
    
help(power)
print(power(2, 5))
