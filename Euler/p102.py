FILE = r"C:\Users\princess\Downloads\p102_triangles.txt"

def parse(file):
    op_file = open(file, "r")
    triangles = []
    for line in op_file.readlines():
        line_split = line[:-1].split(",")
        line_split_int = []
        for num in line_split:
            line_split_int.append(int(num))
        p1 = (line_split_int[0], line_split_int[1])
        p2 = (line_split_int[2], line_split_int[3])
        p3 = (line_split_int[4], line_split_int[5])
        tri = [p1, p2, p3]
        triangles.append(tri)
    return triangles


def triangle_containment(file):
    c = 0
    triangles = parse(file)
    for trig in triangles:
        print(trig)
        if is_contains(trig):
            c += 1
    return c

def is_contains(trig):
    pos = []
    neg = []
    zer = []
    for p in trig:
        if p[1] == 0:
            zer.append(p)
        elif p[1] < 0:
            neg.append(p)
        else:
            pos.append(p)
    if len(pos) == 3 or len(neg) == 3 or len(zer) >= 2 or len(pos) + len(zer) == 3 or len(neg) + len(zer) == 3:
        return False
    if len(pos) == 2 and len(neg) == 1:
        x1 = get_x_intercept(pos[0], neg[0])
        x2 = get_x_intercept(pos[1], neg[0])
    elif len(neg) == 2 and len(pos) == 1:
        x1 = get_x_intercept(neg[0], pos[0])
        x2 = get_x_intercept(neg[1], pos[0])
    elif len(zer) == 1 and len(neg) == 1 and len(pos) == 1:
        x1 = get_x_intercept(neg[0], pos[0])
        x2 = zer[0][0]
    else:
        return False
    return (x1 < 0 and x2 > 0) or (x2 < 0 and x1 > 0)


def get_slope(p1, p2):
    return (p1[1] - p2[1]) / (p1[0] - p2[0])


def get_x_intercept(p1, p2):
    if p1[0] == p2[0]:
        return p1[0]
    m = get_slope(p1, p2)
    x = p1[0]
    y = p1[1]
    return -1*(y / m) + x


print(triangle_containment(FILE))


#print(is_contains([(-340,495), (-153,-910), (835,-947)]))