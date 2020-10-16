class Solution:
    def generate(self, numRows):
        """
        :parameters: numRows: int
        :return: List[List[int]]
        """
        output = []
        for i in range(numRows):
            output.append([1]*(i+1))

        if numRows <= 2:
            return output
        
        for row in range(2, numRows):
            for col in range(1, row):
                output[row][col] = output[row-1][col-1] + output[row-1][col]

        return output

numRows = int(input())
s = Solution()
print(s.generate(numRows))