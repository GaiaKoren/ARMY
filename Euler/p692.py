def get_next_steps(n):
    return list(i for i in range(1, 2*n + 1))


def get_ways(pebbles):
    dic_win = {}
    ways = list([i] for i in range(1, pebbles + 1))
    fin_ways = []
    i = 0
    while len(ways) > 0:
        way = ways[i]
        last_step = way[-1]
        #print(way, last_step)
        for j in range(1, 2 * last_step + 1):
            new_way = way.copy()
            new_way.append(j)
            if sum(new_way) == pebbles:
                fin_ways.append(new_way)
            elif sum(new_way) < pebbles:
                ways.append(new_way)
        ways.remove(way)
    return fin_ways





print(get_ways(4))
