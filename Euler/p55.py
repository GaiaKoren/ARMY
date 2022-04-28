
import math

def is_lychrel(num):
    for i in range(0, 50):
        num += reverse_num(num)
        if is_pal(num):
            return False
    return True



def is_pal(num):
    str_num = str(num)
    half1 = list(str_num[:len(str_num)//2])
    half2 = list(str_num[math.ceil(len(str_num)/2):])
    half2.reverse()
    return half1 == half2

def reverse_num(num):
    num = list(str(num))
    num.reverse()
    num = int("".join(num))
    return num


def lychrel_numbers(lim):
    c = 0
    for i in range(1, lim):
        print(i)
        if is_lychrel(i):
            c += 1
    return c

print(lychrel_numbers(10000))