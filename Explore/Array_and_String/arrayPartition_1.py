class Solution:
    def arrayPairSum(self, nums):
        """
        Group the integers into pairs and make sum of these pairs as large as possible.
        :param nums: List[int]
        :return: int
        """
        if not nums:
            return 0
        if len(nums) % 2 != 0:
            print("Invalid length of nums")
            return 0
        nums = sorted(nums)
        #nums.sort()
        sum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
               sum += nums[i]

        return sum
nums = [1,4,3,2]
s = Solution()
print(s.arrayPairSum(nums))
