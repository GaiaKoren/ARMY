import math


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num <= 0:
        return False
    k = 1
    while 6*k-1 < int(math.sqrt(num+1)):
        if num % (6*k-1) == 0 or num % (6*k+1) == 0:
            return False
        k += 1
    return True

def get_quadratic_primes(a, b):
    n = 0
    num = 2
    c = 0
    while is_prime(num):
        num = n*n + a*n + b
        n += 1
        c += 1
    return c-2

def quadratic_primes(a_lim, b_lim):
    highest_num = 0
    highest_co = []
    for a in range(-1*a_lim+1, a_lim):
        print(a)
        for b in range(-1 * b_lim, b_lim + 1):
            c = get_quadratic_primes(a, b)
            if c > highest_num:
                highest_num = c
                highest_co = [a, b]
    return highest_co, highest_num
print(quadratic_primes(1000, 1000))