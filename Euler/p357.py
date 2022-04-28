import math



def is_special(n, memo):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            s = i + (n / i)
            if memo.get(s) is False:
                return False
    return True

def prime_generating_integers(lim):
    primes = SieveOfEratosthenes(lim)
    s = 0
    i = 1
    while i < lim:
        if primes.get(i) is None and is_special(i-1, primes):
            print(i - 1)
            s += i-1
        i += 2
    return s + 1


def SieveOfEratosthenes(n):
    primes = [True for i in range(n + 1)]
    print("hey")
    p = 2
    memo = {}
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n + 1, p):
                memo[i] = False
                primes[i] = False
        p += 1
    return memo

#print(is_special(6, SieveOfEratosthenes(100)))
print(prime_generating_integers(100000000))