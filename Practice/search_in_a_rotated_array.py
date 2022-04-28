def bin_search(arr, tar, start, end):
    mid = (start + end)//2
    if start > end:
        return -1
    elif arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return bin_search(arr, tar, start, mid-1)
    else:
        return bin_search(arr, tar, mid + 1, end)


def search_rot_index(arr, start, end):
    end_num = arr[end]
    mid = (start + end)//2
    if arr[mid] > arr[mid + 1] or mid == 0:
        return mid
    elif arr[mid] > end_num:
        return search_rot_index(arr, mid + 1, end)
    else:
        return search_rot_index(arr, start, mid-1)
try_arr = [4, 6, 8, 10, 13, 20, 30, 40]



print(search_rot_index(try_arr, 0, len(try_arr)-1))
