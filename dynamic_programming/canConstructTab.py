def canConstruct(target, wordBank):
    table = list(False for i in range(len(target)+1))
    table[0] = True
    pos = 0
    while pos < len(target):
        print(pos)
        for word in wordBank:
            print(word, target[pos:len(word)])
            if word == target[pos:len(word)]:
                print("hey", target[0:pos] + word)
                table[pos+len(word)] = True
        while pos < len(target):
            pos += 1
            if table[pos]:
                print("!", pos)
                break


    print(table)

"""

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
"""




print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))