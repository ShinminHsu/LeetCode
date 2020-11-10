class Solution:
    def findTargetSumWays(self, nums, S):

        self.nums = nums
        self.target = S
        self.memo = {}

        index = len(nums) - 1
        curSum = 0
        
        return self.addSum(index, curSum)
    
    def addSum(self, index, curSum):

        if (index, curSum) in self.memo:
            return self.memo[(index, curSum)]

        if index < 0 and curSum == self.target:
            return 1
        if index < 0:
            return 0

        positive = self.addSum(index-1, curSum + self.nums[index])
        negative = self.addSum(index-1, curSum - self.nums[index])

        self.memo[(index, curSum)] = positive + negative

        return self.memo[(index, curSum)]


nums = [1,1,1,1,1]
S = 3
s = Solution()
print(s.findTargetSumWays(nums, S))
