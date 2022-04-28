from fractions import Fraction
from itertools import combinations
from math import *

def get_fracs_brute(lim):
    fracs = []
    for d in range(1, lim+1):
        print(d)
        for n in range(1, d):
            frac = Fraction(n, d)
            if gcd(n, d) == 1:
                print(frac)
                fracs.append(frac)
    return fracs

def get_prime_facs(n):
    primes = []
    c = 2
    while (n > 1):
        if (n % c == 0):
            if c not in primes:
                primes.append(c)
            n = n / c
        else:
            c = c + 1
    return primes


def get_frac_count(d, memo):
    facs = get_prime_facs(d)
    c = d
    for fac in facs:
        val1 = memo.get(fac)
        val2 = memo.get(fac)
        if val1 is not None and val2 is not None:
            return val1 * val2
        sub = d / fac
        c -= sub
    perms = list(combinations(facs, 2))
    for perm in perms:
        add = d / (perm[0] * perm[1])
        c += add
    return c


def get_fracs(lim, memo):
    c = 0
    for d in range(2, lim+1):
        print(d)
        val = memo.get(d)
        if val is not None:
            c += val
        else:
            c += get_frac_count(d, memo)
    return c


def get_fracs_new(lim, memo):
    c = 0
    for d in range(2, lim+1):
        print("d", d)
        fac = get_fac(d)
        if fac is None:
            memo[d] = d - 1
            print("add", d-1)
            c += d - 1
        else:
            add = memo[fac] * memo[d//fac]
            print("add", add)

            memo[fac*(d//fac)] = add
            c += add
    return c


def get_fac(n):
    c = 2
    while c < n:
        if (n % c == 0):
            return c
        c += 1



def is_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    k = 1
    while 6*k-1 < int(sqrt(num+1)):
        if num % 6*k-1 == 0 or num % 6*k+1 == 0:
            return False
        k += 1
    return True


print(get_fracs_new(int(8), {}))

