import collections

class Solution:
    def updateMatrix(self, matrix):

        nrow, ncol = len(matrix), len(matrix[0])
        memo = [[-1 for _ in range(ncol)] for _ in range(nrow)]
        queue = collections.deque()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(nrow):
            for j in range(ncol):
                # when the cell is 0, then its distance is 0
                if matrix[i][j] == 0:
                    memo[i][j] = 0
                    queue.append((i, j))

        # find the neighbor around the cell which already have the value
        while queue:
            curI, curJ = queue.popleft()
            for i, j in directions:
                neighborI, neighborJ = curI + i, curJ + j
                if (0 <= neighborI < nrow) and (0 <= neighborJ < ncol) and (memo[neighborI][neighborJ] == -1):
                    memo[neighborI][neighborJ] = memo[curI][curJ] + 1
                    queue.append((neighborI, neighborJ))


        return memo

s = Solution()
matrix = [[0],[0],[0]]
print(s.updateMatrix(matrix))
