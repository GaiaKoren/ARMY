def bin_search(arr, tar, start, end):
    mid = (start + end)//2
    if start > end:
        return end
    elif arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return bin_search(arr, tar, start, mid-1)
    else:
        return bin_search(arr, tar, mid + 1, end)


print(bin_search([2, 6, 77, 100, 101, 102], 103, 0, 5))