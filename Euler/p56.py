def powerful_digit_sum(lim):
    res = 0
    for a in range(1, 100):
        print(a)
        for b in range(1, 100):
            p = pow(a, b)
            res = max(sum_digs(p), res)
    return res

def sum_digs(num):
    s = 0
    str_num = str(num)
    l = list(str_num)
    for i in l:
        s += int(i)
    return s

print(powerful_digit_sum(100))