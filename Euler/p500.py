import math


def get_divs(n):
    divs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n / i:
                divs.append(i)
            else:
                divs.append(i)
                divs.append(int(n/i))
    return divs

def get_smallest_divs_brute(count):
    n = 1
    while True:
        if len(get_divs(n)) == count:
            return n
        n += 1

def get_smallest_divs(count):
    div = 1
    c = 0
    n = 1
    while True:
        if c == count:
            return n
        if n % div != 0:
            n *= div
        c += 1
        div += 1

def npr(n, r):
    return math.factorial(n)/math.factorial(n-r)

print(get_divs(get_smallest_divs_brute(17)))
print(get_divs(get_smallest_divs_brute(16)))

#print(get_smallest_divs_brute(50))