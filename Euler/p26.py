import math


def calc_units(l):
    for i in l:
        print(i, 1/i)


def sieve_of_erosthenes(lim):
    nums = list(True for i in range(lim + 1))
    primes = []
    i = 2
    while i < len(nums):
        if nums[i]:
            if i > 500:
                primes.append(i)
            curr = i
            jump = i
            curr += jump
            while curr < len(nums):
                nums[curr] = False
                curr += jump
        i += 1

    return primes

print(calc_units(sieve_of_erosthenes(1000)))
