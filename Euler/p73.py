import math


def get_fracs(d):
    fracs = []
    for n in range(1, d):
        fracs.append(n/d)
    return fracs


def get_fracs_try(d):
    fracs = []
    for n in range(1, d):
        frac = n/d
        if frac > (1/3) and frac < 0.5:
            fracs.append(n/d)
    return fracs

def fracs_in_range_brute(lim):
    fracs = []
    for d in range(1, lim+1):
        print(d)
        for n in range(1, d):
            frac = n / d
            if frac > (1/3) and frac < 0.5 and frac not in fracs:
                fracs.append(frac)
    return len(fracs)


def get_fracs_count(d):
    half = math.floor(d / 2)
    third = math.ceil(d / 3)
    res = half - third + 1
    if half/d == 0.5:
        res -= 1
    if third/d == (1/3):
        res -= 1
    return res


def fracs_in_range(lim):
    dont = {}
    c = 0
    for d in range(lim, 0, -1):
        to_do = dont.get(d)
        if to_do is None:
            print(d)
            for div in get_divs(d):
                dont[div] = False
            c += get_fracs_count(d)
    return c

def create_dic(lim):
    dic = {}
    for i in range(1, lim+1):
        dic[i] = 0
    return dic


def fracs_in_range_try(lim):
    dic = {}
    c = 0
    for d in range(2, lim+1):
        dic[d] = get_fracs_count(d)
    for d in range(2, lim+1):
        c += dic[d]
        curr = 2 * d
        while curr <= lim:
            print(d, curr)
            dic[curr] -= dic[d]
            curr += d
    return c

def get_divs(n):
    divs = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n / i:
                divs.append(i)
            else:
                divs.append(i)
                divs.append(int(n/i))
    return divs

print(fracs_in_range_try(12000))