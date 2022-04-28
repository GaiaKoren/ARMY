import string

PATH = r"C:\Users\princess\Desktop\p042_words.txt"


def parse(path):
    file = open(path, "r")
    names_str = file.read()
    names_str = names_str[1:-1]
    l = names_str.split('","')
    return l


def make_dic():
    lets = list(string.ascii_uppercase)
    dic = {}
    i = 1
    for let in lets:
        dic[let] = i
        i += 1
    return dic

def triangle_numbers(lim):
    nums = []
    n = 1
    curr = 0
    while curr < lim:
        curr = n*(n-1)/2
        nums.append(curr)
        n += 1
    return nums

def coded_triangle_numbers(words):
    dic = make_dic()
    trigs = triangle_numbers(10000)
    res = 0
    for word in words:
        s = 0
        for let in word:
            s += dic[let]
        if s in trigs:
            res += 1
    return res


print(coded_triangle_numbers(parse(PATH)))