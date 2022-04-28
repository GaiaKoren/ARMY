"""
The sieve of Eratosthenes is one of the most efficient ways to find all
primes smaller than n when n is smaller than 10 million or so

time complexity = O(n*log(log(n)))
"""



def sieve_of_erosthenes(lim):
    nums = list(True for i in range(lim + 1))
    primes = []
    i = 2
    while i < len(nums):
        if nums[i]:
            primes.append(i)
            curr = i
            jump = i
            curr += jump
            while curr < len(nums):
                nums[curr] = False
                curr += jump
        i += 1

    return primes

print(sieve_of_erosthenes(1000000))