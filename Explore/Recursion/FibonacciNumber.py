class Solution:
    def fib(self, n: int) -> int:
        hash_map = {0: 0, 1: 1}

        if n in hash_map:
            return hash_map[n]
        
        hash_map[n] = self.fib(n-1) + self.fib(n-2)
        
        return hash_map[n]

import sys

s = Solution()
n = int(sys.argv[1])
print(s.fib(n))