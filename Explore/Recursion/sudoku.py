from typing import List
from collections import defaultdict, deque

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.board = board
        self.candidates()
        val_range = [str(v) for v in range(1, 10)]

        # back tracking
        """
        先從 x = 0, y = 0  開始 (0, 0)，如果他不是 empty 的話，就讓 x 繼續加一，直到為 empty
        """

        def helper():
            if not self.visit:
                return True

            row, col = self.visit.popleft()

            for num in val_range:
                if self.check_value(num, row, col):
                    self.add_value(num, row, col)
                    if helper():  # if every element has been visited
                        return True
                    self.remove_value(num, row, col)
            
            self.visit.appendleft((row, col))
            return False

        helper()

        return self.board
    
    def add_value(self, num, row, col):
        self.row_values[row].add(num)
        self.col_values[col].add(num)
        self.block_values[(row//3, col//3)].add(num)

        self.board[row][col] = num


    def remove_value(self, num, row, col):
        self.row_values[row].remove(num)
        self.col_values[col].remove(num)
        self.block_values[(row//3, col//3)].remove(num)

        self.board[row][col] = '.'

    def candidates(self):
        # 先存下 candidates，以空間換取時間

        self.row_values, self.col_values, self.block_values, self.visit = defaultdict(set), defaultdict(set), defaultdict(set), deque([])

        for row in range(9):
            for col in range(9):
                val = self.board[row][col]
                if val == '.':
                    self.visit.append((row, col))
                else:
                    self.row_values[row].add(val)
                    self.col_values[col].add(val)
                    self.block_values[(row // 3, col // 3)].add(val)
        return

    
    def check_value(self, num, row, col):
        return (num not in self.row_values[row]) and (num not in self.col_values[col]) and (num not in self.block_values[row // 3, col // 3])


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


s = Solution()
return_board = s.solveSudoku(board)

for row in return_board:
    print(row)