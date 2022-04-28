from math import ceil

def bin_search(tar, start, end):
    mid = (start + end)//2
    if start > end:
        return mid
    elif mid*mid == tar:
        return mid
    elif mid*mid > tar:
        return bin_search(tar, start, mid-1)
    else:
        return bin_search(tar, mid + 1, end)

tar = 4
print(bin_search(tar, 1, ceil(tar/2)))