class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums_set = set()

        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            elif num in nums_set:
                nums_set.remove(num)

        return nums_set.pop()
