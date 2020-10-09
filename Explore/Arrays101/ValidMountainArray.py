import sys

class Solution:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False

        up, down = False, False

        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                if down:
                    return False
                else:
                    up = True
            elif A[i-1] > A[i]:
                if not up:
                    return False
                else:
                    down = True
            elif A[i-1] == A[i]:
                return False

        return True if up and down else False

A = list(map(int, sys.stdin.readline().split()))
s = Solution()
print(s.validMountainArray(A))



