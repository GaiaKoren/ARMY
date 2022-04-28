import math

import time
import timeit

memo = {}

def get_tot_rel(n, primes):
    if n in primes:
        memo[n] = n-1
        return n/(n-1)
    dic_val = memo.get(n)
    if dic_val is not None:
        return n/dic_val
    ps, val = get_rel_primes(n)
    memo[n] = val
    for p in ps[1:]:
        memo[p*n] = val * memo[p]
    return n/val

def get_tot_fac(n, primes):
    dic_val = memo.get(n)
    if dic_val is not None:
        return n/dic_val
    val = get_factors(n, primes)
    return n/val

def get_rel_primes(n):
    i = 1
    ps = []
    s = 0
    while i < n:
        if math.gcd(n, i) == 1:
            ps.append(i)
            s += 1
        i += 1
    return ps, s


def tot_max(lim):
    highest = 0
    res = 0
    primes = get_primes(lim + 10)

    for n in range(2, 1000):
        val = get_tot_rel(n, primes)
        if n % 10000 == 0:
            print(n, val)
        if val > highest:
            highest = val
            res = n


    for n in range(1000, lim):
        val = get_tot_fac(n, primes)
        if n % 10000 == 0:
            print(n, val)
        if val > highest:
            highest = val
            res = n
    return res, highest


def tot_max_fac(lim):
    highest = 0
    res = 0
    primes = get_primes(lim + 10)
    for n in range(2, lim):
        val = get_tot_fac(n, primes)
        if n % 10000 == 0:
            print(n, val)
        if val > highest:
            highest = val
            res = n
    return res, highest

def tot_max_p_rel(lim):
    highest = 0
    res = 0
    primes = get_primes(lim + 10)
    for n in range(2, lim):
        val = get_tot_rel(n, primes)
        if n % 10000 == 0:
            print(n, val)
        if val > highest:
            highest = val
            res = n
    return res, highest


def get_primes(lim):
    primes = [True for i in range(lim)]
    primes[0] = False
    primes[1] = False
    i = 2
    while i < lim:
        if primes[i] == True:
            j = 2 * i
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


def get_factors(n, primes):
    res = n
    i = 0
    while primes[i] <= math.sqrt(n):
        if n % primes[i] == 0:
            res *= 1 - (1 / primes[i])
            if int(n/primes[i]) != primes[i]:
                res *= 1-(1/(n/primes[i]))
        i += 1
    return res



start = time.time()

#primes = get_primes(100)

#print(get_rel_primes_bad(1000000))



#print(get_factors(1000000, primes),)
print(tot_max(1000000))
#print(get_factors(9, primes))



end = time.time()
print(end - start)


#print(tot_max(10))

