from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        """
        Naive Approach: iteration O(n)
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0

        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i

        return len(nums)-1
            
class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        
        """
        Binary Search
        如果 middle 在 ascending (nums[mid] < nums[mid+1])，則所求一定在右邊
        如果 middle 在 descending (nums[mid] > nums[mid+1])，則所求一定在左邊
        直到 search space 只剩下一個元素時停止 (left > right)
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid+1]:
                left = mid + 1
            elif nums[mid] > nums[mid+1]:
                right = mid

        return left

nums = [1,3,2,1]
a = Solution2()
print(a.findPeakElement(nums))