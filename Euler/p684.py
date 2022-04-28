def get_dig_sum(num):
    s = 0
    num = list(str(num))
    for dig in num:
        s += int(dig)
    return s


def lowest_dig_sum_brute(num):
    i = 0
    while True:
        if get_dig_sum(i) == num:
            return i
        i += 1

def lowest_dig_sum(num):
    nines_count = (num // 9)
    extra = (num % 9) * pow(10, nines_count)
    nines = pow(10, nines_count)-1
    also_res = extra + nines
    return also_res

def fib_seq(lim):
    prev = 0
    curr = 1
    s = 1
    for i in range(2, lim+1):
        prev, curr = curr, prev + curr
        print(i, curr)
        #s += lowest_dig_sum(curr)

#print(fib_seq(90))

print(lowest_dig_sum(5))


print(lowest_dig_sum(8))


print(lowest_dig_sum(13))


print(lowest_dig_sum(21))


print(lowest_dig_sum(34))


print(lowest_dig_sum(55))


print(lowest_dig_sum(89))

print(lowest_dig_sum(144))


print(lowest_dig_sum(144 + 89))

print(lowest_dig_sum(377))

print(lowest_dig_sum(610))




