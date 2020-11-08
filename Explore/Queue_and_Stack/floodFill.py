class Solution:
    def floodFill(self, image, sr, sc, newColor):

        self.nrow, self.ncol = len(image), len(image[0])
        self.image = image
        self.originalColor = self.image[sr][sc]
        self.newColor = newColor

        if self.originalColor == self.newColor:
            return self.image

        self.DFS(sr, sc)

        return self.image

    def DFS(self, i, j):

        if not (0 <= i < self.nrow) or not (0 <= j < self.ncol):
            return
        if (self.image[i][j] != self.originalColor):
            return

        self.image[i][j] = self.newColor

        self.DFS(i+1, j)
        self.DFS(i-1, j)
        self.DFS(i, j+1)
        self.DFS(i, j-1)

        return

sr, sc = 1, 1
newColor = 1
image = [[0,0,0],[0,1,1]]
s = Solution()
print(s.floodFill(image, sr, sc, newColor))
