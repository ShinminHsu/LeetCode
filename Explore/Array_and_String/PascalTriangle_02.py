class Solution:
    def getRow(self, rowIndex):

        output = []
        for i in range(rowIndex+1):
            output.append([1]*(i+1))

        if rowIndex < 2:
            return output[rowIndex]
        
        for row in range(2, rowIndex+1):

            for col in range(1, row):
                output[row][col] = output[row-1][col-1] + output[row-1][col]

        return output[rowIndex]

numRows = int(input())
s = Solution()
print(s.getRow(numRows))