from itertools import permutations



def check_pro(num):
    fin = 0
    for i in range(1, 5):
        multiplicand = num[:i]
        for j in range(1, 5):
            multiplier = num[i:i+j]
            wish = int(multiplicand) * int(multiplier)
            real = int(num[i+j:])
            if real == wish:
                fin += real
    return fin


def pandigital_multiples():
    pans = permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    s = 0
    i = 0
    for pan in pans:
        print(i)
        num = "".join(list(pan))
        pro = check_pro(num)
        s += pro
        i += 1
    return s


print(pandigital_multiples())
