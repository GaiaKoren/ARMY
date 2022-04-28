try_arr = [2, 4, 8, 10, 12, 14]

def get_missing_number(arr):
    n = len(arr) + 1
    a1 = arr[0]
    d = arr[1] - a1
    an = a1 + (n-1) * d
    expected_sum = (n*(a1 + an))/2
    s = 0
    for num in arr:
        s += num
    return expected_sum - s

print(get_missing_number(try_arr))
