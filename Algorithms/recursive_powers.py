def recursive_powers(base, power):
    if power == 0:
        return 1
    else:
        return base * recursive_powers(base, power-1)

print(recursive_powers(3, 9))

print(pow(3, 9))