def allConstruct(target, wordBank):
    all_ways = []
    if target in wordBank:
        return [target]
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            ways = allConstruct(suffix, wordBank).copy()
            for way in ways:
                op = [word[:len(word)]]
                if type(way) == str:
                    op.append(way)
                else:
                    op += way
                all_ways.append(op)
    return all_ways


def allConstructMemo(target, wordBank, memo):
    all_ways = []
    if target in wordBank:
        return [target]
    val = memo.get(target)
    if val is not None:
        return val
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            ways = allConstructMemo(suffix, wordBank, memo).copy()
            for way in ways:
                op = [word[:len(word)]]
                if type(way) == str:
                    op.append(way)
                else:
                    op += way
                all_ways.append(op)
    memo[target] = all_ways
    return all_ways

print(allConstructMemo("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"], {}))

