def get_primes(lim):
    primes = [True for i in range(lim)]
    primes[0] = False
    primes[1] = False
    i = 2
    while i < lim:
        if primes[i] == True:
            j = 2*i
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



def consecutive_prime_sum(num):
    primes = get_primes(num)
    l = len(primes)
    print(l)
    while l > 0:
        start = 0
        end = l
        print(end, l)
        while end <= l:
            print(primes[start: end])
            start += 1
            end = 1
        l -= 1

print(consecutive_prime_sum(100))


