import timeit

start = timeit.default_timer()




def canConstruct(target, wordBank, curr):
    if curr == target:
        return True
    elif len(curr) > len(target):
        return False
    for word in wordBank:
        comb = curr + word
        print(curr, word, comb)
        if canConstruct(target, wordBank, comb):
            return True
    return False

def canConstructMemo(target, wordBank, curr, memo):
    if curr == target:
        return True
    elif len(curr) > len(target):
        memo[curr] = False
        return False
    val = memo.get(curr)
    if val is not None:
        return val
    for word in wordBank:
        comb = curr + word
        if canConstructMemo(target, wordBank, comb, memo):
            memo[comb] = True
            return True
    return False

def canConstructBetter(target, wordBank, memo):
    if target == "":
        return True
    val = memo.get(target)
    if val is not None:
        return val
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False

print(canConstructMemo("abcdefabcdabde", ["cde", "def", "abcd", "ef"], "", {}))

stop = timeit.default_timer()

print('Time: ', stop - start)