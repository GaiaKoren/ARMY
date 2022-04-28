dic = {}

def canSum(tar, nums, dic):
    if tar == 0:
        return True
    for num in nums:
        temp_tar = tar - num
        val = dic.get(temp_tar)
        if val is not None:
            return val
        if temp_tar < 0:
            dic[temp_tar] = False
            return False
        elif canSum(temp_tar, nums, dic) is True:
            dic[temp_tar] = True
            return True
    dic[temp_tar] = False
    return False


print(canSum(300, [7, 14], dic))