def is_bouncy(num):
    l_num = list(str(num))
    inc = sorted(l_num)
    dec = inc.copy()
    dec.reverse()
    return l_num != inc and l_num != dec

def bouncy_nums(p):
    n = 1
    s = 0
    proportion = s/n
    while proportion != p:
        if is_bouncy(n):
            s += 1
        n += 1
        proportion = s / (n-1)
        print(proportion)
    return s, n-1
print(bouncy_nums(0.99))