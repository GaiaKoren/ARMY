import itertools
import math


def is_two_pal(l):
    og = l.copy()
    l.reverse()
    if og == l and 2 in l:
        return True
    else:
        return False

def get_sum_ways(n):
    curr_ways = [[1, 2], [1, 1, 1]]
    for i in range(4, n+1):
        curr_ways = get_next_ways(curr_ways)
        print(i, len(curr_ways))
    return curr_ways


def get_next_ways(curr_ways):
    ways = []
    for way in curr_ways:
        new_way = way.copy()
        new_way.append(1)
        ways.append(new_way)
        i = 0
        while i < len(way):
            new_way = way.copy()
            new_way[i] += 1
            ways.append(new_way)
            i += 1
    return ways

s = 0
for way in get_sum_ways(10):
    if 2 in way:
        s += 1
print(s)
