class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums)) 
        if len(nums) < 3:
            return max(nums)
        else:
            return sorted(nums)[-3]

nums = list(map(int, input().split()))
s = Solution()
print(s.thirdMax(nums))