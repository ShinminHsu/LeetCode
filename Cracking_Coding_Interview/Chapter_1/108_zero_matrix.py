from typing import List
import unittest

class Solution1:
    def zeroMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        nrow, ncol = len(matrix), len(matrix[0])

        # O(NM)
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    matrix[i][j] = 'v'

        # O(N^2M)
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 'v':

                    for col in range(ncol):
                        if matrix[i][col] != 'v':
                            matrix[i][col] = 0

                    for row in range(nrow):
                        if matrix[row][j] != 'v':
                            matrix[row][j] = 0

        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 'v':
                    matrix[i][j] = 0
        
        return matrix

class Solution2:
    def zeroMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        nrow, ncol = len(matrix), len(matrix[0])

        def mark(row, col, marker = 'v'):
            """Do not modify the original zero but mark other elements in the whole row and the whole column"""
            for i in range(nrow):
                if matrix[i][col] != 0:
                    matrix[i][col] = marker
            
            for i in range(ncol):
                if matrix[row][i] != 0:
                    matrix[row][i] = marker

        # O(NM) mark the places where it should be set to 0
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    mark(i, j)

        # O(NM)
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 'v':
                    matrix[i][j] = 0
        
        return matrix

class Test(unittest.TestCase):
    data = [
        ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
        ([[0,1,2,0],[3,4,5,2],[1,3,1,5]],[[0,0,0,0],[0,4,5,0],[0,3,1,0]])
        ]

    def test_zeroMatrix(self):
        solution = Solution2()
        for test_matrix, answer in self.data:
            result = solution.zeroMatrix(test_matrix)
            self.assertEqual(answer, result)

if __name__ == '__main__':
    unittest.main()