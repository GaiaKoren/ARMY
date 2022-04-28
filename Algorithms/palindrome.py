import math

def is_pal(word, curr):
    print(word[curr], word[len(word)-1 -curr])
    if curr + 1 > math.floor((len(word))/2):
        return True
    if word[curr] == word[len(word)-1 -curr]:
        return is_pal(word, curr+1)
    else:
        return False


print(is_pal("whthhthw", 0))