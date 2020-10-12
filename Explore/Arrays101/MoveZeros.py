class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        zero_index = 0
        for i in range(L):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]  # keep zeros at last
                zero_index += 1

        print(nums)

nums = list(map(int, input().split()))
s = Solution()
s.moveZeroes(nums)
