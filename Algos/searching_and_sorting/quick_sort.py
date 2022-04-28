"""
The key process in quickSort is partition().
Target of partitions is, given an array and an element x of array as pivot,
put x at its correct position in sorted array and put all smaller elements (smaller than x) before x,
and put all greater elements (greater than x) after x.
All this should be done in linear time.

time complexity = O(n2)
"""
my_arr = [10, 80, 40, 90, 30, 50, 70]


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    piv = arr[high]
    i = low - 1
    for j in range(low, high):
        print(piv, arr[j])
        if arr[j] <= piv:
            i += 1
            print("i", i)
            arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return i + 1


print(quick_sort(my_arr, 0, len(my_arr)-1))