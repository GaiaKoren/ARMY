def canSum(targetSum, nums):
    table = list(False for i in range(targetSum+1))
    table[0] = True
    i = 1
    while i < len(table):
        for num in nums:
            if i - num < 0:
                table[i] = False
            else:
                table[i] = table[i - num]
            if table[i] is True:
                break
        i += 1
    return table[targetSum]



print(canSum(300, [7, 3]))