"""
nums = [5,7,7,8,8,10], target = 8

# Find left bound
(1) mid == target: START should be on the left of mid or at mid, set r = mid
(2) mid < target: START should be on the right of mid, set l = mid + 1
(3) mid > target: START should be on the left of mid, set r = mid - 1

-> merge (1) and (3): if mid >= target: r = mid

l, m, r = 0, 2, 5
l, m, r = 3, 4, 5
l, m, r = 3, 3, 4

# Find right bound
(1) mid == target: END should be on the right of mid or at mid, set l = mid
(2) mid < target: END should be on the right of mid, set l = mid + 1
(3) mid > target: END should be on the left of mid, set r = mid - 1

-> merge (1) and (2): if mid <= target: l = mid

"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        result = [-1, -1]

        # Find left bound
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] == target:
            result[0] = left
        else:
            return result

        # Find right bound
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2 + 1   # Make mid biased to the right

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        result[1] = right

        return result

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(is_left):

            left, right = 0, len(nums)

            while left < right:    
                mid = (left + right) // 2

                if (is_left and nums[mid] < target) or (not is_left and nums[mid] <= target):
                    left = mid + 1
                else:
                    right = mid

            return left

        left = binarySearch(is_left=True)
        right = binarySearch(is_left=False)

        if left < len(nums) and nums[left] == target:
            retur;
