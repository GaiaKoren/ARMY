def self_powers(lim):
    s = 0
    for i in range(1, lim + 1):
        s += pow(i, i)
    return s


print(self_powers(1000))