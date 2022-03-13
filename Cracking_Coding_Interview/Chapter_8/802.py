from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        """The solution only check if the robot can arrive at the bottom right"""
        self.count = 0
        self.nrow = len(obstacleGrid)
        self.ncol = len(obstacleGrid[0])

        def dfs(row, col, obstacleGrid):

            if (row >= self.nrow) or (col >= self.ncol) or obstacleGrid[row][col] == 1:
                return False
            
            if (row == self.nrow - 1) and (col == self.ncol - 1):
                return True
            
            return dfs(row + 1, col, obstacleGrid) or dfs(row, col + 1, obstacleGrid)

        return dfs(0, 0, obstacleGrid)

class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        nrow, ncol = len(obstacleGrid), len(obstacleGrid[0])

        answer = [[0 for _ in range(ncol)] for _ in range(nrow)]

        # update the first row
        obstacle = False
        for i in range(ncol):
            if obstacleGrid[0][i] == 1:
                obstacle = True
            if obstacle:
                answer[0][i] = 0
            else:    
                answer[0][i] = 1
            
        # update the first column
        obstacle = False
        for i in range(nrow):
            if obstacleGrid[i][0] == 1:
                obstacle = True
            if obstacle:
                answer[i][0] = 0
            else:    
                answer[i][0] = 1

        # update the whole grid
        for i in range(nrow):
            for j in range(ncol):
                if obstacleGrid[i][j] == 1:
                    answer[i][j] = 0
                else:
                    answer[i][j] = answer[i - 1][j] + answer[i][j - 1]

        return answer[nrow - 1][ncol - 1]

obstacleGrid = [
    [0, '#', '#', 0],
    [0,  0,  '#', 0],
    [0,  0,   0,  0]
]

s = Solution()
print(s.uniquePathsWithObstacles(obstacleGrid))