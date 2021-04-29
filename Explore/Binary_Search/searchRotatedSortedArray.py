from typing import List

class Solution1:
    def search(self, nums: List[int], target: int) -> int:

        # find minimum value in the list to divide into two separte list
        def find_minimum(nums):
            left, right = 0, len(nums) - 1
            
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[right]:
                    # then min value will be in the right half
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def find_half_list(cutoff_index, nums, target):
            if cutoff_index == 0:
                start, end = 0, len(nums) - 1
            elif nums[0] <= target:
                start, end = 0, cutoff_index - 1
            else:
                start, end = cutoff_index, len(nums) - 1
            return start, end

        def binary_search(start, end, nums, target):
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1

            return -1

        cutoff_index = find_minimum(nums)
        start, end = find_half_list(cutoff_index, nums, target)
        
        return binary_search(start, end, nums, target)

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

nums = [4,5,7,0,1,2,3]
target = 0
s = Solution2()
print(s.search(nums, target))