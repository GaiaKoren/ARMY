import math


def get_lim(dic):
    num = "9"
    while True:
        if int(num) > get_fac(dic, num):
            return int(num)
        num += "9"

def facs():
    dic = {}
    for i in range(10):
        dic[i] = math.factorial(i)
    return dic


def get_fac(dic, num):
    s = 0
    for dig in num:
        s += dic[int(dig)]
    return s

def digit_factorial(lim):
    dic = facs()
    s = -3
    for i in range(lim):
        if i == get_fac(dic, str(i)):
            print(i)
            s += i
        i += 1
    return s

print(digit_factorial(get_lim(facs())))