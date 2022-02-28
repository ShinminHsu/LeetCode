from typing import List
import unittest

def rotateMatrix(matrix: List[List[int]]) -> List[List[int]]:

    n = len(matrix)

    for i in range(n // 2 + n % 2):
        for j in range(n // 2):

            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = tmp

    return matrix

class Test(unittest.TestCase):
    data = [
        ([[1,2,3], [4,5,6], [7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
        ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
    ]

    def test_rotate(self):
        for test_matrix, answer in self.data:
            result = rotateMatrix(test_matrix)
            self.assertEqual(answer, result)

if __name__ == '__main__':
    unittest.main()