def pentagon_numbers(lim):
    nums = []
    n = 1
    curr = 0
    while curr < lim:
        curr = n*(3*n-1)/2
        nums.append(curr)
        n += 1
    return nums

def triangle_numbers(lim):
    nums = []
    n = 1
    curr = 0
    while curr < lim:
        curr = n*(n-1)/2
        nums.append(curr)
        n += 1
    return nums

def hexagonal_numbers(lim):
    nums = []
    n = 1
    curr = 0
    while curr < lim:
        curr = n*(2*n-1)
        nums.append(curr)
        n += 1
    return nums


def in_all():
    res = []
    lim =3000000000
    trigs = triangle_numbers(lim)
    pents = pentagon_numbers(lim)
    hex = hexagonal_numbers(lim)
    for trig in trigs:
        print(trig)
        if trig in pents and trig in hex:
            res.append(trig)
    return res

print(in_all())
