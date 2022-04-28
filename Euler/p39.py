import math


def integer_right_triangles(lim):
    dict = {}
    i = 1
    while i <= lim:
        dict[i] = 0
        i += 1
    for a in range(1, lim):
        for b in range(1, lim):
            p = math.sqrt(pow(a, 2) + pow(b, 2)) + a + b
            if p <= 1000 and p.is_integer():
                dict[p] += 1
    m = 0
    res = 0
    for key in dict.keys():
        if dict[key] > m:
            m = dict[key]
            res = key
    return res

print(integer_right_triangles(1000))
