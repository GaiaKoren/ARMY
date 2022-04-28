dic = {}

def bestSum(tar, nums):
    if tar == 0:
        return []
    if tar < 0:
        return None
    res = None
    for num in nums:
        temp_tar = tar - num
        new_l = bestSum(temp_tar, nums)
        if new_l is not None:
            new_l.append(num)
        if new_l is not None and (res is None or len(res) > len(new_l)):
            res = new_l
    print(tar, res)
    return res


def bestSumMemo(tar, nums, memo):
    val = memo.get(tar)
    if val is not None:
        return val.copy()
    if tar == 0:
        return []
    if tar < 0:
        return None
    res = None
    for num in nums:
        temp_tar = tar - num
        new_l = bestSumMemo(temp_tar, nums, memo)
        if new_l is not None:
            new_l.append(num)
        if new_l is not None and (res is None or len(res) > len(new_l)):
            res = new_l
    memo[tar] = res.copy()
    return res

print(bestSumMemo(100, [1, 2, 5, 50, 25], dic))