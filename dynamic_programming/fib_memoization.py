dic = {1: 1, 2: 1}

def recurs_fib(n):
    val = dic.get(n)
    if val is not None:
        return val
    dic[n] = recurs_fib(n-1) + recurs_fib(n-2)
    return dic[n]

print(recurs_fib(50))