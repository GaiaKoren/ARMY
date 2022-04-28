def bestSum(targetSum, nums):
    table = list(None for i in range(targetSum+1))
    table[0] = []
    i = 1
    while i < len(table):
        best_way = None
        for num in nums:
            if i - num < 0 or table[i - num] is None:
                table[i] = None
            else:
                res = table[i - num].copy()
                res.append(num)
                if best_way is None or len(res) < len(best_way):
                    best_way = res
        table[i] = best_way
        i += 1
    return table[targetSum]



print(bestSum(30, [3, 4, 2, 5]))