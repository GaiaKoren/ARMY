from fractions import Fraction

memo = {}

def get_iter(n):
    if n == 1:
        return (Fraction(1, 2))
    val = memo.get(n)
    if val is not None:
        return val
    prev = get_iter(n-1)
    iteration = Fraction(1/(2+prev))
    memo[n] = iteration
    return iteration


def sqaure_root_convergents(lim):
    count = 0
    for i in range(1, lim+1):
        num = get_iter(i) + 1
        if len(str(num.numerator)) > len(str(num.denominator)):
            count += 1
    return count

print(sqaure_root_convergents(1000))