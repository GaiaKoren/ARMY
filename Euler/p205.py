import math
from itertools import combinations_with_replacement


def get_cube_probs():
    probs = {}
    my_npr = npr(6, 6)
    combs = list(combinations_with_replacement([1, 2, 3, 4, 5, 6], 6))
    for comb in combs:
        s = sum(comb)
        if probs.get(s) is None:
            probs[s] = my_npr/(pow(6, 6))
        else:
            probs[s] += my_npr/(pow(6, 6))
    return probs

def get_pyr_probs():
    probs = {}
    my_npr = npr(9, 9)
    combs = list(combinations_with_replacement([1, 2, 3, 4], 9))
    for comb in combs:
        s = sum(comb)
        if probs.get(s) is None:
            probs[s] = my_npr/(pow(4, 9))
        else:
            probs[s] += my_npr/(pow(4, 9))
    return probs


def npr(n, r):
    return math.factorial(n)/math.factorial(n-r)

def dice_game():
    s = 0

    cube_probs = get_cube_probs()
    pyr_probs = get_pyr_probs()
    for cube_key in cube_probs:
        for pyr_key in pyr_probs:
            if pyr_key > cube_key:
                prob = cube_probs[cube_key] * pyr_probs[pyr_key]
                s += prob
    return s, round(s, 7)

print(dice_game())