def missing_number(arr):
    i = 0
    while i < len(arr):
        ind = arr[i]
        if ind < 0:
            ind *= -1
        ind -= 1
        if ind < len(arr):
            arr[ind] *= -1
        i += 1
    i = 0
    while i < len(arr):
        if arr[i] > 0:
            return i + 1
        i += 1
    return len(arr)

def rem_negs(arr):
    i = 0
    len_arr = len(arr)
    while i < len_arr:
        if arr[i] <= 0:
            arr.pop(i)
            len_arr = len(arr)
        else:
            i += 1
    return arr

def solution(arr):
    return missing_number((rem_negs(arr)))

print(solution([0,-10,1,3,-20]))

