import math


def get_smallest_num(div):
    curr = 1
    for i in range(2, div + 1):
        curr *= i
        if curr % div == 0:
            return i

def divisibility_of_factorials_brute(lim):
    s = 0
    for i in range(2, lim+1):
        res = get_smallest_num(i)
        s += res
        res_try = largest_prime_factor(i)
        print(i, res, res_try)
        """
        if res_try[1]:
            print(i, res, res_try[0])
        """
    return s


def largest_prime_factor(n):
    og = n
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n, og % pow(n, 2) != 0


def largest_div(n):
    m = 0
    i = 2
    c = 0
    while i <= math.sqrt(n):
        if (n % i == 0):
            m = max(m, i, n/i)
        i = i + 1
    return m



def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    prime_nums = []
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def divisibility_of_factorials(lim):
    primes = SieveOfEratosthenes(lim)
    s = 0
    i = 2
    while i < len(primes):
        if primes[i]:
            print("new prime", i)
            num = i
            res = num
            while num <= lim:
                print("this", res-1, lim//num)
                print(min(res-1, lim//num))
                s += num * min(res-1, lim//num)
                num = pow(num, 2)
                res = get_smallest_num(num)
                print(num, res)
            print("sum", s)

        i += 1
    return s
print(divisibility_of_factorials_brute(100000))

