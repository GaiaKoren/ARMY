primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def comp(num1, tar):
    if num1 == tar:
        return True
    elif num1 > tar:
        return "left"
    else:
        return "right"



def binary_search_loop(nums, target):
    start = 0
    end = len(nums) - 1
    while True:
        mid = round((end + start) / 2)
        res = comp(nums[mid], target)
        if res is True:
            return mid
        elif res == "right":
            start = mid
        else:
            end = mid

def binary_search_recurs(nums, target, start, end):
    mid = round((end + start) / 2)
    res = comp(nums[mid], target)
    if res is True:
        return mid
    if res == "right":
        start = mid
        return binary_search_recurs(nums, target, start, end)
    else:
        end = mid
        return binary_search_recurs(nums, target, start, end)


print(binary_search_recurs(primes, 97, 0, 24))
