import math


def is_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    k = 1
    while 6*k-1 < int(math.sqrt(num+1)):
        if num % 6*k-1 == 0 or num % 6*k+1 == 0:
            return False
        k += 1
    return True


print(is_prime(43))