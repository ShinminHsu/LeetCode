class Solution:
    def pivotIndex(self, nums):
        sum_all = sum(nums)
        sum_left = 0
        n = len(nums)

        for i in range(n):
            if sum_left == sum_all - nums[i] - sum_left:
                return i

            sum_left += nums[i]

        return -1

nums = list(map(int, input().split()))
s = Solution()
print(s.pivotIndex(nums))