try_arr = [2, 5, 3, 1]

def get_missing_number(arr):
    n = len(arr) + 1
    expected_sum = (n*(1 + n))/2
    s = 0
    for num in arr:
        s += num
    return expected_sum - s

print(get_missing_number(try_arr))
