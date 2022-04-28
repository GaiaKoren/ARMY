"""
If n is a prime number, then for every a, 1 < a < n-1,

an-1 ≡ 1 (mod n)
 OR
an-1 % n = 1 


Time complexity = O(k Log n)
pow func takes log n time
"""



import random

def fermet_method(num, k):
    if num == 1 or num == 4:
        return False
    elif num == 2 or num == 3:
        return True
    for i in range(k):
        n = random.randint(2, num - 2)
        if pow(n, num - 1, num) != 1:
            return False
    return True


print(fermet_method(4949, 6))