


def countConstruct(target, wordBank):
    ways = 0
    if target == "":
        return 1
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            ways += countConstruct(suffix, wordBank)
    return ways

def countConstructMemo(target, wordBank, memo):
    ways = 0
    if target == "":
        return 1
    val = memo.get(target)
    if val is not None:
        return val
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            ways += countConstructMemo(suffix, wordBank, memo)
    memo[target] = ways
    return ways

print(countConstructMemo("aaab", ["a", "b", "ab", "aa"], {}))


