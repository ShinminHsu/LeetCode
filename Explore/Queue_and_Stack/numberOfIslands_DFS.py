class Solution:
    def numIslands(self, grid) -> int:

        if not grid:
            return 0
        self.grid = grid
        self.nrow, self.ncol = len(grid), len(grid[0])

        return sum(self.DFS(i, j) for i in range(self.nrow) for j in range(self.ncol) if self.grid[i][j] == "1")


    def DFS(self, i, j):

        if not (0 <= i < self.nrow) or not (0 <= j < self.ncol) or self.grid[i][j] != "1":
            return 0

        self.grid[i][j] = "V"

        self.DFS(i+1, j)
        self.DFS(i-1, j)
        self.DFS(i, j+1)
        self.DFS(i, j-1)

        return 1
    