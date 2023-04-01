def dfs(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
        return

    grid[row][col] = "0"
    dfs(grid, row - 1, col)
    dfs(grid, row + 1, col)
    dfs(grid, row, col - 1)
    dfs(grid, row, col + 1)


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        num_of_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    num_of_islands += 1

        return num_of_islands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["0", "0", "0", "1", "1"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "1", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
