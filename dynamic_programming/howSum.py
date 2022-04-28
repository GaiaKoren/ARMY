dic = {}

def howSum(tar, nums, dic):
    if tar == 0:
        return []
    if tar < 0:
        return None
    for num in nums:
        temp_tar = tar - num
        val = dic.get(temp_tar)
        if val is not None:
            val.append(num)
            return val
        new_l = howSum(temp_tar, nums, dic)
        if new_l is not None:
            new_l.append(num)
            val = dic.get(temp_tar)
            if val is None:
                dic[temp_tar] = new_l
            return dic[temp_tar]


print(howSum(8, [3, 4, 7, 8], dic))