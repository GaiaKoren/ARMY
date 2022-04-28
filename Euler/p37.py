memo = {}


def is_trunct(num, primes):
    i = 1
    num = str(num)
    while i < len(num):
        if memo.get(num[i:]) is False or memo.get(num[:i]) is False:
            print(num)
            memo[num] = False
            return False
        if int(num[i:]) not in primes or int(num[:i]) not in primes:
            memo[num] = False
            return False
        i += 1
    return True


def get_primes(lim):
    primes = [True for i in range(lim)]
    primes[0] = False
    primes[1] = False
    i = 2
    while i < lim:
        if primes[i] == True:
            j = 2 * i
            while j < lim:
                primes[j] = False
                j += i

        i += 1
    fin = []
    i = 0
    while i < len(primes):
        if primes[i]:
            fin.append(i)
        i += 1
    return fin


def truncatable_primes():
    primes = get_primes(1000000)
    c = 0
    i = 4
    s = 0
    while c != 11:
        if is_trunct(primes[i], primes):
            s += primes[i]
            c += 1
        i += 1

    return s


print(truncatable_primes())
