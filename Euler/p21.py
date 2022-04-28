import math




def amicable_nums(lim):
    dic = {}
    for i in range(1, lim):
        s = get_divs_sum(i)
        dic[i] = s
    s = 0
    for key in dic:
        if key == dic.get(dic[key]) and key != dic[key]:
            print(key, dic[key])
            s += key
            print(key, s)
    return s



def get_divs_sum(n):
    divs = []
    i = 1
    while i <= math.sqrt(n) + 1:
        if (n % i == 0):
            divs.append(i)
            divs.append(n/i)
        i = i + 1
    return sum(divs) - 1*n
print(amicable_nums(10000))
