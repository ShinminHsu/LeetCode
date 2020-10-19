class Solution():
    def minSubArrayLen(self, s, nums):
        """
        :param numbers: int
        :param target: List[int]
        :return: int
        """

        i, j, n = 0, 0, len(nums)
        minLen = float("inf")
        curSum = 0

        while j < n:
            if j < n and curSum < s:
                curSum += nums[j]
                j += 1
            elif i < j and curSum > s:
                curSum -= nums[i]
                i -= 1

        