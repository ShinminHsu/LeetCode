class Solution:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            digit = 0
            while num:
                num, _ = divmod(num, 10)
                digit += 1
            
            if digit % 2 == 0:
                count += 1
                
        return count

nums = [12,345,2,6,7869]
s = Solution()
print(s.findNumbers(nums))