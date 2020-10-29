class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.

        :param nums: List[int]
        :param k: int
        :return None
        """
        if not nums or k == 0:
            return

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
            

nums = [1,2]
k = 0
s = Solution()
s.rotate(nums, k)
print(nums)