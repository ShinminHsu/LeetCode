from typing import List

class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

        self.puzzle = [['.' for _ in range(n)] for _ in range(n)]
        self.count = 0
        self.n = n
        
        # try to put the queen on the n_row row
        def nqueens(nrow):
            if nrow == self.n:
                self.count += 1
                return

            for ncol in range(n):
                if self.is_in_attack(nrow, ncol):
                    continue
                
                self.puzzle[nrow][ncol] = 'Q'
                nqueens(nrow + 1)  # find the next row
                self.puzzle[nrow][ncol] = '.'  # remove

        
        nqueens(0)

        return self.count


    def check_dia(self, row, col, row_step, col_step):
        n_row, n_col = row, col

        while n_row >= 0 and n_col >= 0 and n_row < self.n and n_col < self.n:
            if self.puzzle[n_row][n_col] == 'Q':
                return True
            n_row += row_step
            n_col += col_step
            
        return False
    
    def is_in_attack(self, row, col):
        # check col
        if any([s == 'Q' for s in self.puzzle[row]]):
            return True
        if self.check_dia(row, col, 1, 1) or self.check_dia(row, col, 1, -1) or self.check_dia(row, col, -1, 1) or self.check_dia(row, col, -1, -1):
            return True
        
        return False

        
        
class Solution2:
    def totalNQueens(self, n: int) -> List[List[str]]:

        self.puzzle = [['.' for _ in range(n)] for _ in range(n)]
        self.count = 0
        self.n = n

        self.cols = [False for _ in range(n)]
        self.dia1 = [False for _ in range(2*n-1)]
        self.dia2 = [False for _ in range(2*n-1)]
        
        # try to put the queen on the n_row row
        def nqueens(nrow):
            if nrow == self.n:
                self.count += 1
                return

            for ncol in range(n):
                if self.is_in_attack(nrow, ncol):
                    continue
                
                self.updateBoard(self, nrow, ncol, True)
                nqueens(nrow + 1)  # find the next row
                self.updateBoard(self, nrow, ncol, False)   # remove

        nqueens(0)

        return self.count

    def updateBoard(self, nrow, ncol, put):
        self.cols[ncol] = put
        self.dia1[nrow + ncol] = put
        self.dia2[ncol - nrow + self.n - 1] = put
        self.puzzle[nrow][ncol] = 'Q' if put else '.'

    
    def is_in_attack(self, nrow, ncol):
        return self.cols[ncol] or self.dia1[nrow + ncol] or self.dia2[ncol - nrow + self.n - 1]


class Solution3:
    def totalNQueens(self, n: int) -> List[List[str]]:

        usedCols = set()
        usedDia1 = set()
        usedDia2 = set()

        return self.helper(0, n, usedCols, usedDia1, usedDia2)

    def helper(self, nrow, n, usedCols, usedDia1, usedDia2):
        count = 0

        if nrow == n:
            return 1

        for ncol in range(n):
            if self.is_in_attack(self, ncol, nrow, usedCols, usedDia1, usedDia2):
                continue
            
            self.updateBoard(nrow, ncol, True, usedCols, usedDia1, usedDia2)
            count += self.helper(nrow + 1, n, usedCols, usedDia1, usedDia2)  # find the next row
            self.updateBoard(nrow, ncol, False, usedCols, usedDia1, usedDia2)   # remove

        return count

    def updateBoard(self, nrow, ncol, put, usedCols, usedDia1, usedDia2):
        self.cols[ncol] = put
        self.dia1[nrow + ncol] = put
        self.dia2[ncol - nrow + self.n - 1] = put

    
    def is_in_attack(self, ncol, nrow, usedCols, usedDia1, usedDia2):
        return (ncol in usedCols) or (nrow + ncol in usedDia1) or (ncol - nrow in usedDia2)



n = 4
s = Solution()
print(s.solveNQueens(4))

