
nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]




def calc(list, add):
    i = 0
    while True:
        i = i + add
        div = True
        for a in list:
            if i % a != 0:
                div = False
        if div == True:
            return i

print(calc(nums, 2520))

