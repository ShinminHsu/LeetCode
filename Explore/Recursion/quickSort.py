class Solution:
    def quicksort(self, nums):

        if len(nums) == 1:
            return nums

        self.helper(nums, 0, len(nums) - 1)

        return nums


    def helper(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.helper(nums, left, pivot - 1)
            self.helper(nums, pivot + 1, right)

    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left

        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[right] = nums[right], nums[i]

        return i

nums = [1, 5, 3, 2, 8, 7, 6, 4]
s = Solution()
print(s.quicksort(nums))