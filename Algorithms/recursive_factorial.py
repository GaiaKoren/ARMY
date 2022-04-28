def recursive_factorial(fac):
    if fac == 0:
        return 1
    return fac * recursive_factorial(fac - 1)

print(recursive_factorial(5))