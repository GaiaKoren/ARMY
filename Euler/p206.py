import itertools
import math

def is_concealed(n):
    str_n = str(n)
    i = 0
    real = 1
    if len(str_n) != 19:
        return False
    if str_n[-1] != "0":
        return False
    while i < len(str_n)-2:
        if str_n[i] != str(real):
            return False
        i += 2
        real += 1
    return True


def concealed_square_old():
    i = int(math.sqrt(1020304050607080900))
    lim = int(math.sqrt(19293949596979899990))
    while True:
        sq = pow(i, 2)
        print(lim-i)
        if is_concealed(sq):
            return sq
        i += 1


def concealed_square(opts):
    curr_opts = []
    if len(opts[0]) == 9:
        return opts
    for opt in opts:
        print(opt, len(opt))
        for i in range(9):
            new_opt = opt + str(i)
            curr_opts.append(new_opt)
    curr_opts = concealed_square(curr_opts)
    return curr_opts

print(concealed_square_old())



