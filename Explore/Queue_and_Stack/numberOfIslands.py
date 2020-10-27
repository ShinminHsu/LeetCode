from queue import Queue

class Solution:
    def numIslands(self, grid) -> int:

        if not grid:
            return 0
        self.grid = grid
        self.nrow, self.ncol = len(grid), len(grid[0])

        return sum(self.BFS(i, j) for i in range(self.nrow) for j in range(self.ncol) if self.grid[i][j] == "1")


    def BFS(self, i, j):
        lands, self.grid[i][j] = Queue(), "V"
        lands.put([i, j])

        while lands.qsize() > 0:
            i, j = lands.get()
            # check if there are adjacent lands around (i, j)
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < self.nrow and 0 <= y < self.ncol and self.grid[x][y] == "1":
                    lands.put([x, y])
                    self.grid[x][y] = "V"

        return 1


grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
s = Solution()
print(s.numIslands(grid))



