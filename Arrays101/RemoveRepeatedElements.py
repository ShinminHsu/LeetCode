class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return
        
        prev = nums[0]
        length = 0

        for i, num in enumerate(nums):
            if num != prev:
                print(num)
                nums[length] = prev
                length += 1
                prev = num

            nums[length] = prev
        nums[:] = nums[:length+1]

        print(nums)

nums = [1,1,2]
s = Solution()
s.removeDuplicates(nums)
print(nums)