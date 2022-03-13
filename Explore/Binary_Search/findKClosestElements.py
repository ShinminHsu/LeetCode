"""
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

l, r, m = 0, 4, 2
l, r, m = 0, 1, 0
l, r, m = 0, -1, 

"""


from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        left, right = 0, len(arr) - 1

        def binarySearch(left, right):

            while left < right:
                mid = (left + right) // 2

                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    left = mid + 1
                elif arr[mid] > x:
                    right = mid - 1

            return left

        left = binarySearch(left, right)

        if left > k:
            return arr[left-k:left]
        else:
            return arr[:k]
            

class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        sorted_arr = sorted(arr, key=lambda num: abs(x - num))

        return sorted(sorted_arr[:k])

class Solution3:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        left, right = 0, len(arr) - k

        while left < right:

            mid = (left + right) // 2

            if abs(arr[mid+k] - x) >= abs(arr[mid] - x):
                right = mid
            elif abs(arr[mid+k] - x) < abs(arr[mid] - x):
                left = mid + 1

        return arr[left:left+k]
            