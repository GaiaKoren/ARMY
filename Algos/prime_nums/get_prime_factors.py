"""
Time Complexity: This Approach is best for all composite numbers and achieves O(log n) but is O(n) otherwise.
"""



def primeFactors(n):
    primes = []
    c = 2
    while (n > 1):

        if (n % c == 0):
            primes.append(c)
            n = n / c
        else:
            c = c + 1
    return primes

n = 315
print(primeFactors(n))