"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def get_prime(limit):
    primes = []
    curr_num = 2
    while len(primes) <= limit-1:
        print(curr_num)
        prime = True
        for p in primes:
            if curr_num % p == 0:
                prime = False
                break
        if prime is True:
            primes.append(curr_num)
        curr_num = curr_num + 1
    return primes[-1]





print(get_prime(10001))