import math


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


def primeFactors(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            primes.append(int(i))

            n = n / i
    if n > 2:
        primes.append(int(n))
    return primes

def is_cube_full(n):
    for fac in primeFactors(n):
        if n % (fac**3) != 0:
            return False
    return True


def get_cube_divs(n):
    c = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n / i:
                if is_cube_full(i):
                    c += 1
            else:
                if is_cube_full(i):
                    c += 1
                if is_cube_full(int(n/i)):
                    c += 1
    return c


def cube_full_divisors(lim):
    s = 0
    for i in range(1, lim+1):
        print(i)
        s += get_cube_divs(i)
    return s


def get_divs_count(lim):
    p3s = get_cube_fulls(lim)
    print(p3s)
    i = 1
    ops = 0
    for p1 in p3s:
        print(p1)
        ops += int(math.log(lim, p1))
        for p2 in p3s[i:]:
            #print(p1, p2)
            pro = p1 * p2
            if pro > lim:
                break
            ops += get_nums(p1, p2, lim)
        i += 1
    return ops


def get_nums(p1, p2, lim):
    prods_num = 0
    lim1 = int(math.log(lim, p1))
    lim2 = int(math.log(lim, p2))
    for i in range(3, lim1+1):
        for j in range(3, lim2+1):
            pro = p1**i * p2**j
            if pro > lim:
                break
            prods_num += 1
    return prods_num


def get_cube_fulls_brute(lim):
    cfs = []
    for i in range(1, lim+1):
        if is_cube_full(i):
            cfs.append(i)
    return cfs

#print(get_cube_fulls_brute(16))

print(cube_full_divisors(16))