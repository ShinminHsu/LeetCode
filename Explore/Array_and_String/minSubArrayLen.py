class Solution():
    def minSubArrayLen(self, s, nums):
        """
        :param numbers: int
        :param target: List[int]
        :return: int
        """
        if not nums:
            return 0

        i, j, n = 0, 0, len(nums)
        minLen = float("inf")
        curSum = 0

        while j < n:
            while j < n and curSum < s:
                curSum += nums[j]
                j += 1
            while i < j and curSum >= s:
                curSum -= nums[i]
                i += 1
            minLen = min(minLen, j-i+1)

        return minLen if minLen <= n else 0

solution = Solution()
nums = [2,3,1,2,4]
s = 7
print(solution.minSubArrayLen(s, nums))
