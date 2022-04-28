def is_harsh(num):
    return num % sum_of_digs(num) == 0

def is_strong(num):
    res = num / sum_of_digs(num)
    return is_prime(res)

def sum_of_digs(num):
    digs = str(num)
    s = 0
    for dig in digs:
        s += int(dig)
    return s

def get_harsh_nums(lim):
    nums = [""]
    j = 0
    new_num = 0
    while int(new_num) < lim:
        for i in range(10):
            new_num = nums[j] + str(i)
            if int(new_num) >= lim:
                return nums[1:]
            if new_num != "0" and is_harsh(int(new_num)):
                nums.append(new_num)

        j += 1


def is_prime(num):
    if num == 1:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def harshad_numbers(lim):
    s = 0
    harshes = get_harsh_nums(lim//10)
    primes = []
    for harsh in harshes:
        if is_strong(int(harsh)):
            for i in range(10):
                new_num = int(harsh + str(i))
                if is_prime(new_num):
                    primes.append(new_num)
                    s += new_num
    return s, sum(primes), primes
print(harshad_numbers(pow(10, 14)))
