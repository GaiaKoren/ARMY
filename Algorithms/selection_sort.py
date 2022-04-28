

numbers = [22, 11, 99, 88, 9, 7, 42]


def selection_sort(nums, loc):
    if loc == len(nums):
        return nums
    i = nums.index(min(nums[loc:]))
    val = nums[i]
    nums[i] = nums[loc]
    nums[loc] = val
    loc = loc + 1
    return selection_sort(nums, loc)

print(selection_sort(numbers, 0))