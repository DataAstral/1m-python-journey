# TASK 8 — NESTED LIST (2D GRID)

grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(grid[1][2])
print(grid[1])
print(grid[-1][-1])

for row in grid:
    for el in row:
        print(el)
