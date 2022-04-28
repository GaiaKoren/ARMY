import math
from itertools import permutations


def is_cube(num):
    res = num**(1/3)
    if res.is_integer():
        return True
    c = math.ceil(res)
    if c**3 == num:
        return True
    return False



def cubes_count(base):
    goods = []
    digs = str(base**3)
    perms = list(permutations(digs))
    for perm in perms:
        if perm[0] == "0":
            continue
        n = int("".join(perm))
        if is_cube(n):
            if n not in goods:
                goods.append(n)
    return len(goods)

def cubic_permutations_brute(amount):
    n = 1
    while True:
        print(n)
        c = cubes_count(n)
        if c == amount:
            return n
        n += 1

def cubic_permutations(amount):
    memo = {}
    n = 1
    while True:
        print(n)
        in_order = list(str(n**3))
        in_order.sort()
        in_order = "".join(in_order)
        val = memo.get(in_order)
        if val is None:
            memo[in_order] = [n**3]
        else:
            memo[in_order].append(n**3)
        if len(memo[in_order]) == amount:
            return memo[in_order]
        n += 1

#print(is_cube(10))
#print(cubes_count(100))
print(cubic_permutations(5))
