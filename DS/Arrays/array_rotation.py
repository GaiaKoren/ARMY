"""
https://www.geeksforgeeks.org/array-rotation/

Write a function rotate(ar[], d) that rotates arr[] of size n by d elements.


"""

my_arr = [1, 2, 3, 4, 5]


def rotate(arr, d):
    d = -d
    half1 = arr[:d]
    half2 = arr[d:]
    arr = half2 + half1

    return arr

print(rotate(my_arr, 1))