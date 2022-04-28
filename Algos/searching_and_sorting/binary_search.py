"""
Binary Search Algorithm: The basic steps to perform Binary Search are:

Begin with an interval covering the whole array.
If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
Otherwise, narrow it to the upper half.
Repeatedly check until the value is found or the interval is empty.

time complexity = O(Log n)
"""




arr = [1, 2, 4, 6, 9, 20]

def bin_search(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        print(start, end, mid)
        if arr[mid] < num:
            start = mid+1
        elif arr[mid] > num:
            end = mid-1
        if arr[mid] == num:
            return mid


print(bin_search(arr, 11))
