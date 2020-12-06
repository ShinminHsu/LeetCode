class Solution:
    def search(self, nums, target):

        def binary(left, right):
            if left >= right:
                return -1

            index = (right - left) // 2 + left

            if nums[index] == target:
                return index
            elif nums[index] < target:
                return binary(index + 1, right)
            elif target < nums[index]:
                return binary(left, index)

            return -1

        return binary(0, len(nums) - 1)

s = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(s.search(nums, target))
