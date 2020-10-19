class Solution:
    def twoSum(self, numbers, target):
        """
        Given an array of integers that is already sorted in ascending order,
        find two numbers such that they add up to a specific target number.

        :param numbers: List[int]
        :param target: int
        :return: List[int]
        """
        if not numbers:
            return []

        hash_table = {}
        for i, num in enumerate(numbers):
            
            diff = target - num
            if diff in hash_table:
                return [hash_table[diff] + 1, i+ 1]

            else:
                hash_table[num] = i

        return []

numbers = [0,0]
target = 0
s = Solution()
print(s.twoSum(numbers, target))