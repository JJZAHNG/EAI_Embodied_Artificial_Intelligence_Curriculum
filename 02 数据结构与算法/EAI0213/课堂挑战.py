map = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]


memo = {}

def min_energy(x, y, grid):
    if x >= len(grid) or y >= len(grid[0]):
        return float('inf')  # 越界

    if (x, y) in memo:
        return memo[(x, y)]

    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        return grid[x][y]  # 到终点

    down = min_energy(x + 1, y, grid)
    right = min_energy(x, y + 1, grid)
    memo[(x, y)] = grid[x][y] + min(down, right)

    return memo[(x, y)]


