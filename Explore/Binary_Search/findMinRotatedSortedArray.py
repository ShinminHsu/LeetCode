from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        def binarySearch(left, right):

            if left >= right:
                return nums[left]

            mid = left + (right - left) // 2

            if nums[left] < nums[mid]:
                if nums[mid] > nums[right]:
                    return binarySearch(mid+1, right)
                else:
                    return binarySearch(left, mid)

            else:
                if nums[mid] > nums[right]:
                    return binarySearch(mid+1, right)
                else:
                    return binarySearch(left, mid)

        return binarySearch(left, right)