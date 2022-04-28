def fib(tar):
    table = [0 for i in range(0, tar+1)]
    table[1] = 1
    a = 0
    while a+1 <= tar:
        table[a+1] += table[a]
        if a+2 <= tar:
            table[a+2] += table[a]
        a += 1
    return table[tar]

print(fib(10))