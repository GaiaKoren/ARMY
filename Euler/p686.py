from math import *

from itertools import *



def is_starts(num, digs):
    if str(num)[:2] == str(digs):
        return True
    return False

def brute_powers_of_two(lim):
    for i in range(lim):
        res = pow(2, i)
        print(i, res)
        if is_starts(res, 12):
            print(res)

print(pow(0.5, 7))
print(pow(0.5, 12710))


