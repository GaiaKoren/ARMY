from itertools import permutations


def get_trigs(lim):
    shapes = []
    shape = 1
    n = 2
    while shape <= lim:
        if shape >= 1000:
            shapes.append(shape)
        shape = n*(n+1)/2
        n += 1
    return shapes

def get_squares(lim):
    shapes = []
    shape = 1
    n = 2
    while shape <= lim:
        if shape >= 1000:
            shapes.append(shape)
        shape = n**2
        n += 1
    return shapes

def get_pents(lim):
    shapes = []
    shape = 1
    n = 2
    while shape <= lim:
        if shape >= 1000:
            shapes.append(shape)
        shape = n*(3*n-1)/2
        n += 1
    return shapes



def get_hexs(lim):
    shapes = []
    shape = 1
    n = 2
    while shape <= lim:
        if shape >= 1000:
            shapes.append(shape)
        shape = n*(2*n-1)
        n += 1
    return shapes

def get_hepts(lim):
    shapes = []
    shape = 1
    n = 2
    while shape <= lim:
        if shape >= 1000:
            shapes.append(shape)
        shape = n*(5*n-3)/2
        n += 1
    return shapes


def get_octs(lim):
    shapes = []
    shape = 1
    n = 2
    while shape <= lim:
        if shape >= 1000:
            shapes.append(shape)
        shape = n*(3*n-2)
        n += 1
    return shapes


def cyclical_figurate_numbers(lim):
    trigs = get_trigs(lim)
    squares = get_squares(lim)
    pents = get_pents(lim)
    hexs = get_hexs(lim)
    hepts = get_hepts(lim)
    octs = get_octs(lim)
    combs = []

    for hx in hexs:
        for hp in hepts:
            for oct in octs:
                combs.append([hx, hp, oct])
    print(len(combs))


    """
    
        for t in trigs:
        for s in squares:
            for p in pents:
                comb = [str(int(t)), str(int(s)), str(int(p))]
                #print(int(t), int(s), int(p))
                res = id_state(comb)
                print(res)
    
    """



def id_state(nums):
    perms = permutations(nums)
    res = []
    for perm in perms:
        num1 = perm[0]
        num2 = perm[1]
        num3 = perm[2]
        if num1[2:] == num2[:2] and num2[2:] == num3[:2]:
            res.append([1, perm])
        elif num1[2:] == num2[:2]:
            res.append([2, perm])
        else:
            res.append([3, perm])
    return res

def id_state(nums):
    perms = permutations(nums)
    res = []
    for perm in perms:
        num1 = perm[0]
        num2 = perm[1]
        num3 = perm[2]
        if num1[2:] == num2[:2] and num2[2:] == num3[:2]:
            res.append([1, perm])
        elif num1[2:] == num2[:2]:
            res.append([2, perm])
        else:
            res.append([3, perm])
    return res



#print(id_state([str(8128), str(2882), str(8281)]))



def is_cyclic(nums, new_num):
    first_num = nums[0]
    last_num = nums[-1]
    if first_num[:2] == new_num[-2:]:
        nums = [new_num] + nums
    elif last_num[-2:] == new_num[:2]:
        nums = nums.append(new_num)
    else:
        return False
    return nums



print(cyclical_figurate_numbers(9000))

