import random

"""
Use the second template of Binary Search
We need to find the first one
"""

class Solution:

    def __init__(self, n):
        self.bad_version = self.createBadVersion(n)

    def createBadVersion(self, n):
        return random.randint(1,n)

    def isBadVersion(self, version):
        return version >= self.bad_version

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 0, n

        while left < right:
            mid  = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        if self.isBadVersion(left):
            return left
        
        return left + 1

while True:
    n = random.randint(1, 100)
    solution = Solution(n)
    if solution.bad_version != solution.firstBadVersion(n):
        print(solution.bad_version, solution.firstBadVersion(n))
