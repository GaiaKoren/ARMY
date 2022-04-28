import math


def get_perf_squares(lim):
    perf_squares = {}
    n = int(math.sqrt(lim)) + 1
    while 0 < n:
        my_pow = pow(n, 2)
        res = lim // my_pow
        perf_squares[int(my_pow)] = int(res)
        print(my_pow)
        n -= 1
    return perf_squares


def sum_of_squares(lim):
    dic = get_perf_squares(lim)
    print(dic)
    ones = 2*dic[1]
    s = 0
    for key in dic:
        s += key * dic[key]
        ones -= dic[key]
        print(key, dic[key], s)
        for i in range(1, int(math.sqrt(key)) + 1):
            if key % i == 0:
                val1 = dic.get(i)
                if val1 is not None:
                    dic[i] = val1 - dic[key]
                val2 = dic.get(key/i)
                if val2 is not None and key != key/i:
                    dic[int(key/i)] = val2 - dic[key]
    dic[1] = ones
    print(ones)
    return s

def get_divs(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            print(i, int(num/i))

#print(get_divs(784))

print(sum_of_squares(pow(10, 2)))

