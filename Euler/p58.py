import math
import random

from pip._vendor.urllib3.connectionpool import xrange


def spiral_primes():
    primes = 0
    all_nums = 1
    length = 3
    curr = 1
    while True:
        jump = length - 1
        i = 1
        while i <= 4:
            curr += jump
            if is_prime(curr, 40):
                primes += 1
            all_nums += 1
            i += 1
        if primes / all_nums < 0.1:
            return length
        if length % 10000 == 1:
            print("ratio", primes / all_nums, curr)
        length += 2

def is_prime(n, k):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r = 0
    d = n-1
    while d % 2 == 0:
        d = d / 2
        r += 1
    i = 0
    while i < k:
        if not miller_test(n, d):
            return False
        i += 1
    return True

def miller_test(n, d):
    a = 2 + random.randint(1, n - 4)
    x = pow(int(a), int(d), n)
    if x == 1 or x == n-1:
        return True
    while d != n-1:
        x = (pow(x, 2)) % n
        d *= 2
        if x == 1:
            return False
        elif x == n-1:
            return True
    return False

print(spiral_primes())