import math


def get_fac_sum(num):
    s = 0
    digs = list(str(num))
    for dig in digs:
        s += math.factorial(int(dig))
    return s

def get_fac_chain(num):
    chain_length = 1
    while num != 145 and num != 169 and num != 871 and num != 872:
        num = get_fac_sum(num)
        chain_length += 1
    return chain_length


print(get_fac_chain(78))