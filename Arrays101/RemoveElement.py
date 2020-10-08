class Solution:
    def removeElement(self, nums, val):
        L = len(nums) - 1

        for i in reversed(nums):
            if i == val:
                nums[i], nums[L] = nums[L], nums[i]
                L -= 1

        nums = nums[:L+1]

nums, val = [3,2,2,3], 3
s = Solution()
s.removeElement(nums, val)
print(nums)
