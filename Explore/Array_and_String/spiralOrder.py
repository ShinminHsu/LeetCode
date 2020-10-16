class Solution:
    def spiralOrder(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: List[int]
        """
        if not matrix: return []

        nrow, ncol = len(matrix), len(matrix[0])
        size = nrow * ncol
        r, l, u, d = ncol - 1, 0, 0, nrow - 1  # boundaries
        ouput = []

        while len(ouput) < size:

            # top row, turn right
            if len(ouput) < size:
                ouput.extend(matrix[u][j] for j in range(l, r+1))
            u += 1
            
            # right column, turn down
            if len(ouput) < size:
                ouput.extend(matrix[i][r] for i in range(u, d+1))
            r -= 1
            
            # bottom row, turn left
            if len(ouput) < size:
                ouput.extend(matrix[d][j] for j in range(r, l-1, -1))
            d -= 1
            
            # left column, turn up
            if len(ouput) < size:
                ouput.extend(matrix[i][l] for i in range(d, u-1, -1))
            l += 1

        return ouput

matrix = [
 [ 1, 2, 3, 10, 13 ],
 [ 4, 5, 6, 11, 14 ],
 [ 7, 8, 9, 12, 15 ],
 [ 16, 17, 18, 19, 20]
]

s = Solution()
print(s.spiralOrder(matrix))
