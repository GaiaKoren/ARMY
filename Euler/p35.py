import itertools

def get_primes(lim):
    primes = [True for i in range(lim)]
    primes[0] = False
    primes[1] = False
    i = 2
    while i < lim:
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

from itertools import cycle



def get_circs(num):
    l = list(str(num))
    pool = cycle(l)
    all_res = []
    for a in range(len(l)):
        next(pool)
        i = 0
        res = ""
        while i < len(l):
            res += next(pool)
            i += 1
        all_res.append(int(res))
    return all_res



def circular_primes(lim):
    count = 0
    primes = get_primes(lim)
    i = 0
    while i < len(primes):
        print(i, len(primes))
        prime = primes[i]
        circs = get_circs(prime)
        is_circ = True
        for circ in circs:
            if circ not in primes:
                primes.remove(prime)
                is_circ = False
                break
        if is_circ is True:
            count += 1
            i += 1

    return count

print(circular_primes(1000000))

