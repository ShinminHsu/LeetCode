class Solution:
    def twoSum(self, nums, target):
        hash_table  = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_table and i != hash_table[diff]:
                return [hash_table[diff], i]
            else:
                hash_table[num] = i
