def bin_search_first(arr, tar, start, end):
    mid = (start + end)//2
    if start > end:
        return -1
    elif arr[mid] == tar and arr[mid-1] < tar:
        return mid
    elif arr[mid] > tar or arr[mid] == tar:
        return bin_search_first(arr, tar, start, mid-1)
    else:
        return bin_search_first(arr, tar, mid + 1, end)

def bin_search_last(arr, tar, start, end):
    mid = (start + end)//2
    if start > end:
        return -1
    elif arr[mid] == tar and arr[mid+1] > tar:
        return mid
    elif arr[mid] > tar:
        return bin_search_last(arr, tar, start, mid-1)
    else:
        return bin_search_last(arr, tar, mid + 1, end)

def num_of_occurrences(arr, tar):
    end = len(arr) - 1
    return bin_search_last(arr, tar, 0, end) - bin_search_first(arr, tar, 0, end) + 1

try_arr = [4, 6, 8, 8, 8, 8, 10, 20, 30, 40]

print(bin_search_first(try_arr, 6, 0, len(try_arr)-1))
print(bin_search_last(try_arr, 6, 0, len(try_arr)-1))
print(num_of_occurrences(try_arr, 6))