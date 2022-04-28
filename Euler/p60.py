import math
from itertools import combinations



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

def get_prime_combs(primes, r):
    for p1 in primes:
        print("p1", p1)
        for p2 in primes:
            #print("p2", p1)
            if not is_comb_prime(p1, [p2]):
                continue
            for p3 in primes:
                #print("p3", p3)
                if not is_comb_prime(p3, [p1, p2]):
                    continue
                for p4 in primes:
                    #print("p4", p4)
                    if not is_comb_prime(p4, [p1, p2, p3]):
                        continue
                    for p5 in primes:
                        #print("p5", p5)
                        if is_comb_prime(p5, [p1, p2, p3, p4]):
                            return [p1, p2, p3, p4, p5]


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num <= 0:
        return False
    k = 1
    while 6*k-1 < int(math.sqrt(num+1)):
        if num % (6*k-1) == 0 or num % (6*k+1) == 0:
            return False
        k += 1
    return True


def is_comb_prime(p1, primes):
    for p2 in primes:
        if p1 == p2 or not is_prime(int(str(p1) + str(p2))) or not is_prime(int(str(p2) + str(p1))):
            return False
    return True


def is_combs_prime(primes):
    combs = combinations(primes, 2)
    for comb in combs:
        if not is_prime(int(str(comb[0]) + str(comb[1]))) or not is_prime(int(str(comb[1]) + str(comb[0]))):
            return False
    return True


#print(is_combs_prime((3, 7, 109, 673)))

print(get_prime_combs(sieve_of_erosthenes(10000), 5))