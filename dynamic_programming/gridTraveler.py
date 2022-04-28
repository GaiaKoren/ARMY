

def gridTraveler(line, column):
    if grid[line][column] != 0:
        return grid[line][column]
    if line == 0 or column == 0:
        grid[line][column] = 1
        return 1
    grid[line][column] = gridTraveler(line-1, column) + gridTraveler(line, column-1)
    return grid[line][column]

def get_grid(length):
    grid = list(range(length))
    i = 0
    while i < len(grid):
        grid[i] = [0] * length
        i += 1
    return grid

grid = get_grid(21)

print(gridTraveler(20, 20))