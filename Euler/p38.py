from itertools import permutations



def check_conc(num):
    str_num = str(num)
    for i in range(1, 5):
        is_conc = True
        og = str_num[:i]
        j = i
        times = 2
        while True:
            next_num = int(og) * times
            len_next_num = len(str(next_num))
            if next_num != int(str_num[j: j + len_next_num]):
                is_conc = False
                break
            times += 1
            j += len_next_num
            if j == 9 and is_conc is True:
                return True
    return is_conc

def pandigital_multiples():
    pans = permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    m = 0
    for pan in pans:
        num = int("".join(list(pan)))
        if check_conc(num):
            m = max(m, num)
    return m
print(pandigital_multiples())