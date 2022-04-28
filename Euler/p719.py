import math

from itertools import permutations
def get_all_sums(half1, half2):
    all_sums = []
    for s1 in half1:
        for s2 in half2:
            all_sums.append(s1 + s2)
    return all_sums
memo = {}
real_ways = []
def is_sum(n, real_n):
    global memo
    if n < 10:
        return [n]
    val = memo.get(n)
    if val is not None:
        print("yes")
        return val
    digs = str(n)
    len_num = len(digs)
    for i in range(1, len_num):
        split_point = i
        part1 = digs[:split_point]
        part2 = digs[split_point:]
        sums1 = is_sum(int(part1), real_n)
        sums2 = is_sum(int(part2), real_n)

        ways = get_all_sums(sums1, sums2)
        ways.append(n)
        memo[n] = ways
        if n == real_n:
            global real_ways
            real_ways += ways
    return ways



def number_splitting(lim):
    s = 0
    i = 2
    while i <= math.sqrt(lim):
        square = pow(i, 2)
        print(square, lim)
        global real_ways

        is_sum(square, square)
        for way in real_ways:
            if way == i:
                print(True, square, way)
                s += square
                break
        real_ways = []
        i += 1
    return s


print(number_splitting(pow(10, 4)))


def get_perf_squares(lim):
    s = 0
    i = 2
    while i <= math.sqrt(lim):
        square = pow(i, 2)
        print(square)
        s += square
        i += 1
    return s


