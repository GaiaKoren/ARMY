import math

FILE = r"C:\Users\princess\Desktop\p345.txt"



def parse(file):
    op_file = open(file, "r")
    lines = op_file.readlines()
    fin = []
    for line in lines:
        new_line = []
        for num in line[:-1].split(" "):
            new_line.append(int(num))
        fin.append(new_line)
    fin[-1][-1] = 805
    return fin


def matrix_sum(file):
    lines = parse(file)
    dic = {}
    res = []
    n = 0
    for line in lines:
        sub = 0
        for i in range(1, len(line)):
            m = get_num(line, i)
            val = dic.get(m)
            if val is None:
                dic[m] = n
                break
            else:

                
        n += 1
    return dic



def get_num(line, place):
    new_line = sorted(line)
    return line.index(new_line[-1*place])

print(matrix_sum(FILE))

