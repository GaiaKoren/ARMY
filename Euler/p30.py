import math


def get_lim():
    num = "9"
    while True:
        if int(num) > get_pow(num):
            return int(num)
        num += "9"


def get_pow(num):
    s = 0
    for dig in num:
        s += pow(int(dig), 5)
    return s

def digit_fifth_powers(lim):
    s = -1
    for i in range(lim):
        print(i, lim)
        if i == get_pow(str(i)):
            s += i
        i += 1
    return s

print(digit_fifth_powers(get_lim()))