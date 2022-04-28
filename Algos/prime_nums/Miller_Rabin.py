import random


def isPrime(n, k):
    if n == 2 or n == 3:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    d = n-1
    r = 0
    while d % 2 == 0:
        d /= 2
        r += 1
    for i in range(k):
        print(i)
        if not miller_test(n, d, r):
            return False
    return True

def miller_test(n, d, r):
    a = random.randint(2, n-2)
    x = pow(a, d) % n
    if x == 1 or x == n-1:
        return True
    for i in range(r-1):
        x = pow(x, 2) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False


print(isPrime(49, 40))
