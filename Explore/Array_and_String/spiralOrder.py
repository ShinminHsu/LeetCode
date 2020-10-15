class Solution:
    def spiralOrder(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: List[int]
        """

        if not matrix:
            return []

        nrow, ncol = len(matrix), len(matrix[0])

        r, l, u, d = nrow - 1, 0, 0, ncol - 1  # boundaries


