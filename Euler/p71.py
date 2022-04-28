def generate_fractions(lim):
    fracs = []
    for d in range(2, lim+1):
        print(d)
        for n in range(1, d):
            fracs.append(n/d)
    fracs = list(set(fracs))
    fracs.sort()
    return fracs

print(generate_fractions(1000000))
