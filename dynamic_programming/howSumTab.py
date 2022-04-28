def howSum(targetSum, nums):
    table = list(None for i in range(targetSum+1))
    table[0] = []
    i = 1
    while i < len(table):
        for num in nums:
            if i - num < 0 or table[i - num] is None:
                table[i] = None
            else:
                res = table[i - num].copy()
                res.append(num)
                table[i] = res
                break
        i += 1
    return table[targetSum]



print(howSum(30, [5, 3, 4, 2]))