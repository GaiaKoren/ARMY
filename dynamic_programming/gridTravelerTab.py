def gridTraveler(line, column):
    grid = get_grid(line)
    i = 0
    while i < line:
        grid[0][i] = 1
        i += 1
    i = 0
    while i < column:
        grid[i][0] = 1
        i += 1
    l = 1
    while l < line:
        c = 1
        while c < column:
            grid[l][c] = grid[l-1][c] + grid[l][c-1]
            c += 1
        l += 1
    return grid[line-1][column-1]




def get_grid(length):
    grid = list(range(length))
    i = 0
    while i < len(grid):
        grid[i] = [0] * length
        i += 1
    return grid


print(gridTraveler(3, 3))