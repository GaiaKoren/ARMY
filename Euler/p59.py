import string
import itertools

FILE = r"C:\Users\princess\Downloads\p059_cipher.txt"



def parse(file):
    opened_file = open(file, 'r')
    txt_list = opened_file.read().split(',')
    return txt_list



def turn_to_lets(nums, pwd):
    txt = ""
    i = 1
    for num in nums:
        if i % 3 == 0:
            let = chr((int(num) ^ pwd[2]))
        elif i % 3 == 1:
            let = chr((int(num) ^ pwd[0]))
        else:
            let = chr((int(num) ^ pwd[1]))
        txt += let
        i += 1
    return txt


def create_ascii_table():
    dic = {}
    i = 97
    for let in string.ascii_lowercase:
        dic[i] = let
        i += 1
    return dic

def get_ascii_nums():
    nums = []
    i = 97
    for let in string.ascii_lowercase:
        nums.append(i)
        i += 1
    return nums

def xor_decryption(file):
    nums_list = parse(file)
    pwds = generate_passwords()
    i = 0
    for pwd in pwds:
        txt = turn_to_lets(nums_list, pwd)
        i += 1
        if txt.count(' ') > 50 and txt.count(' a ') >= 1:
            print(pwd, txt)
    return None


def generate_passwords():
    ops = get_ascii_nums()
    pwds = list(itertools.permutations(ops, 3))
    return pwds


def sum_of_scii_vals(file):
    nums = parse(file)
    pwd = [101, 120, 112]
    txt = turn_to_lets(nums, pwd)
    s = 0
    for let in txt:
        s += ord(let)
    return s
print(sum_of_scii_vals(FILE))

#print(xor_decryption(FILE))

