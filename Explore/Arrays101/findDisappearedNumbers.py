class Solution:
    def findDisappearedNumbers(self, nums):

        disappeared = []
        if not nums:
            return disappeared

        n = len(nums)
        nums = set(nums)

        for i in range(1, n+1):
            if i not in nums:
                disappeared.append(i)

        return disappeared

nums = list(map(int, input().split()))
s = Solution()
print(s.findDisappearedNumbers(nums))

