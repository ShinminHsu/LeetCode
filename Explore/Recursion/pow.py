class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            
            if n % 2 == 0:
                return helper(x * x, n // 2)

            else:
                return x * helper(x * x, n // 2)

        if n < 0:
            return 1 / helper(x, abs(n))

        else:
            return helper(x, n)

import sys

s = Solution()
x, n = float(sys.argv[1]), int(sys.argv[2])
print(s.myPow(x, n))