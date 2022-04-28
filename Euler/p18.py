FILE = r"C:\Users\princess\PycharmProjects\REAL\Euler\p18.txt"


def parse(file):
    file = open(file, "r")
    file_str = file.read()
    full_list = file_str.split("\n")
    all_lists = []
    for l in full_list:
        curr_list = l.split(" ")
        i = 0
        for num in curr_list:
            curr_list[i] = int(num)
            i = i + 1
        all_lists.append((curr_list))
    return all_lists


def get_max(lists):
    tris = []
    a = 1
    while a < len(lists):
        print(lists[a])
        i = 0
        while i < len(lists[a]):
            print(lists[a][i])

            m_num = lists[a][i]
            s_num1 = lists[a-1][i]
            s_num2 = lists[a-1][i+1]

            print(m_num, s_num1, s_num2)
            tri = max(m_num + s_num1, m_num + s_num2)
            print(tri)
            tris.append(tri)
            i = i + 1
        lists[a] = tris.copy()
        tris = []
        a = a + 1
    return lists[-1]




result = parse(FILE)
result.reverse()
print(get_max(result))