import math
import timeit

import time

start = time.time()
print("hello")




def primeFactors(n):
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

def is_dist(n, p, q):
    c = 2
    while (n > 1):
        if (n % c == 0):
            if c != p and c != q:
                return False
            n = n / c
        else:
            c = c + 1
    return True

def get_all_dists_brute(N):
    memo = {}
    dists = []
    for num in range(N, 0, -1):
        facs = primeFactors(num)
        if len(facs) == 2:
            facs[0] = str(facs[0])
            facs[1] = str(facs[1])
            facs_str = " ".join(facs)
            if memo.get(facs_str) is None:
                print(num)
                dists.append([num, facs])
                memo[facs_str] = True
    return dists

def sieve_of_erosthenes(lim):
    nums = list(True for i in range(lim + 1))
    primes = []
    i = 2
    while i < len(nums):
        if nums[i]:
            primes.append(i)
            curr = i
            jump = i
            curr += jump
            while curr < len(nums):
                nums[curr] = False
                curr += jump
        i += 1

    return primes



def get_all_bases(lim):
    bases = []
    bases_fin = []
    primes = sieve_of_erosthenes(int(lim/2))
    i = 0
    for prime1 in primes:
        i += 1
        for prime2 in primes[i:]:
            prod = prime1*prime2
            if prod > lim:
                break
            print(prod, prime1, prime2)
            if prod * prime1 > lim and prod * prime2 > lim:
                bases_fin.append(prod)
            else:
                bases.append(prod)
    return bases, bases_fin

def get_all_bases_try(lim):
    bases = 0
    primes = sieve_of_erosthenes(int(lim/2))
    i = 0
    for prime1 in primes:
        i += 1
        if prime1 * primes[i] > lim:
            break
        for prime2 in primes[i:]:
            prod = prime1*prime2
            if prod > lim:
                break
            #print(prime1, prime2, prod)
            bases += get_highest(prime1, prime2, lim)
    return bases

def get_highest(p1, p2, lim):
    highest = 0
    p1_lim = math.log(lim, p1)
    p2_lim = math.log(lim, p2)
    pow1 = 1
    while pow1 <= p1_lim:
        pow2 = 1
        while pow2 <= p2_lim:
            res = pow(p2, pow2) * pow(p1, pow1)
            if res > lim:
                break
            highest = max(res, highest)
            pow2 += 1
        pow1 += 1
    return highest


print(get_all_bases_try(pow(10, 7)))
end = time.time()
print(end - start)
#print(len(get_all_dists_brute(100)))
#print(len(sieve_of_erosthenes(5*pow(10, 6))))
