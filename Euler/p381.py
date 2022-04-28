import math


def get_sp(p, k):
    s = 0
    if math.factorial(p-1) % p == 0:
        return 0
    for k in range(1, k+1):
        fac = math.factorial(p-k)
        s += fac
    return s % p

def prime_k_factorial_brute(start, end):
    s = 0
    primes = sieve_of_erosthenes(end)
    for p in primes:
        if p < start:
            continue
        #print(p, get_sp(p, 5))
        s += get_sp(p, 5)
    return s

def all_k_factorial_brute(start, end):
    s = 0
    for p in range(start, end):
        #print(p, get_sp(p, 5))
        s += get_sp(p, 5)
    return s - 9

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

print(prime_k_factorial_brute(5, pow(10, 4)))
print(all_k_factorial_brute(5, pow(10, 4)))
#print(sieve_of_erosthenes(pow(10, 8)))
