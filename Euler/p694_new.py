import math
from itertools import combinations

def get_cube(num):
    res = num**(1/3)
    c = math.ceil(res)
    if c**3 == num:
        return c
    return res



def get_cube_fulls(lim):
    lim = int(lim**(1/3))
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


def get_divs(lim):
    p3s = get_cube_fulls(lim)
    i = 1
    ops = []
    for p1 in p3s:
        for p2 in p3s[i:]:
            pro = p1 * p2
            if pro > lim:
                break
            ops.append([p1, p2])
        i += 1
    return ops


def get_divs_new(lim):
    p3s = get_cube_fulls(lim)
    print(p3s)
    c = lim
    for p in p3s:
        for i in range(3, int(math.log(lim, p)) + 1):
            c += math.floor(lim/(p**i))
    i = 1
    for p1 in p3s:
        for p2 in p3s[i:]:
            print(p1, p2)
            pro = pow(p1, 3) * pow(p2, 3)
            if pro > lim:
                break
            c += get_divs_nums(p1, p2, lim)
        i += 1
    return c

def get_divs_nums(p1, p2, lim):
    c = 0
    p1_lim = int(math.log(lim, p1))
    p2_lim = int(math.log(lim, p2))
    print(p1_lim, p2_lim)
    for i in range(3, p1_lim+1):
        for j in range(3, p2_lim+1):
            pro = pow(p1, i) * pow(p2, j)
            if pro > lim:
                break
            c += 1
    return c

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


def get_divs_real(n):
    divs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n / i:
                divs.append(i)
            else:
                divs.append(i)
                divs.append(int(n/i))
    return divs

def cube_full_divs_brute(lim):
    c = 0
    for n in range(1, lim + 1):
        n_count = 0
        for div in get_divs_real(n):
            if is_cube_full(div):

                n_count += 1
        print(n, n_count)
        c += n_count
    return c

#print(cube_full_divs_brute(10000))
print(get_divs_new(10000))

#ops, ops_done = get_divs(pow(10, 4))

#print(len(ops), len(ops_done))


#print(get_nums(8, 27, pow(10, 18)))

#print(get_cube_fulls(pow(10, 18)))

#print(get_divs(pow(10, 18)))