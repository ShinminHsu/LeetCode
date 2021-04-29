from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        def helper(start, end):

            if start >= end:
                if nums[start] == target:
                    return start
                else:
                    return -1

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return helper(mid + 1, end)
            elif target < nums[mid]:
                return helper(start, mid)
            

        return helper(0, len(nums) - 1)

class Solution2:
    def search(self, nums: List[int], target: int) -> int:        
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

        