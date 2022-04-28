from fractions import Fraction
from itertools import combinations
from math import *
from functools import reduce


def get_fracs_brute(lim):
    fracs = []
    for d in range(1, lim+1):
        for n in range(1, d):
            frac = Fraction(n, d)
            if gcd(n, d) == 1:
                fracs.append(frac)
    return fracs



def counting_fractions(lim):
    memo = {}
    c = 0
    for n in range(lim, 1, -1):
        print(n)
        val = memo.get(n)
        if val == False:
            continue
        for fac in get_divs(n):
            memo[fac] = False
        c += n - 1
        print("c", c)
    return c


def get_divs(n):
    divs = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if i == n / i:
                divs.append(i)
            else:
                divs.append(i)
                divs.append(int(n/i))
    return divs


def prime_factors(n):
    primes = set()
    c = 2
    while (n > 1):

        if (n % c == 0):
            primes.add(c)
            n = n / c
        else:
            c = c + 1
    return primes


def prime_factor(n):
    c = 2
    while True:
        if (n % c == 0):
            return c
        else:
            c = c + 1


def get_facs_brute(d):
    facs = prime_factors(d)
    c = 0
    for n in range(1, d + 1):
        is_good = True
        for fac in facs:
            if n % fac == 0:
                is_good = False
                break
        if is_good:
            c += 1
    return c

def get_facs1(d):
    facs = prime_factors(d)
    print(facs)
    res = d
    for fac in facs:
        res -= d/fac
    print(res)
    for i in range(2, len(facs)+1):
        combs = combinations(facs, i)
        combs = list(combs)
        for comb in combs:
            res += d / (reduce((lambda x, y: x * y), comb))
    return res
print(get_facs_brute(21))

print(get_facs1(21))



