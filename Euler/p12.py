import math


def get_trig(n):
    return n*(n+1)/2



def get_divs(n):
    divs = 0
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0):
            if (n / i == i):
                divs += 1
            else:
                divs += 2

        i = i + 1
    return divs

def highly_divisible_triangular_number():
    n = 1
    t = 1
    while True:
        print(t)
        t = get_trig(n)
        if get_divs(t) > 500:
            return t
        n += 1

print(highly_divisible_triangular_number())