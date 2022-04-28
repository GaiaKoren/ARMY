import math
from itertools import permutations

def get_primes(lim):
    primes = [True for i in range(lim)]
    primes[0] = False
    primes[1] = False
    i = 2
    while i < lim:
        print(i)
        if primes[i] == True:
            j = 2*i
            while j < lim:
                primes[j] = False
                j += i

        i += 1
    fin = []
    i = 0
    while i < len(primes):
        if primes[i]:
            fin.append(i)
        i += 1
    return fin


def is_prime(num):
    if num > 1:
        for i in range(2, math.ceil(num/2)):
            if (num % i) == 0:
                return False
    return True


def pandigital_primes():
    high = 0
    perms = list(permutations("1234567"))
    i = 0
    for perm in perms:
        if i % 100:
            print(i, len(perms))
        num = int("".join(perm))
        if is_prime(num):
            high = max(high, num)
        i += 1
    return high

print(pandigital_primes())

