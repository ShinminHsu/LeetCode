class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return matrix

        n_row, n_col = len(matrix), len(matrix[0])
        diagonal = {k: [] for k in range((n_row-1) + n_col)}
        output = []

        for row in range(n_row):
            for col in range(n_col):
                diagonal[row + col].append(matrix[row][col])
        print(diagonal)
        for index in diagonal:
            if index % 2 == 1:
                output.extend(diagonal[index])
            else:
                output.extend(reversed(diagonal[index]))

        return output

matrix = [
 [1,2,3,4],[5,6,7,8]
]

s = Solution()
print(s.findDiagonalOrder(matrix))
