"""
It divides the input array into two halves,
calls itself for the two halves, and then merges the two sorted halves.


time complexity = θ(nLogn)
"""


def merge(arr1, arr2):
    mer_array = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            mer_array.append(arr1[i])
            i += 1
        else:
            mer_array.append(arr2[j])
            j += 1
    if i < len(arr1):
        mer_array += arr1[i:]
    elif j < len(arr2):
        mer_array += arr2[j:]
    return mer_array

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        half1 = arr[:mid]
        half2 = arr[mid:]
        half1 = merge_sort(half1)
        half2 = merge_sort(half2)
        print(half1, half2)
        arr = merge(half1, half2)
    return arr

my_arr = [10, 80, 40, 90, 30, 50, 70]

print(merge_sort(my_arr))