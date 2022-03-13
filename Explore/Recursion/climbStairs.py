class Solution:
    def climbStairs(self, n: int) -> int:
        hash_map = {1: 1, 2: 2}

        for i in range(3, n+1):
            hash_map[i] = hash_map[i-1] + hash_map[i-2]

        return hash_map[n]

class Solution2:
    def climbStairs(self, n: int) -> int:
        hash_map = {1: 1, 2: 2}

        def helper(i):
            if i in hash_map:
                return hash_map[i]
            hash_map[i] = helper(i-1) + helper(i-2)

        return hash_map[n]

class Solution3:
    def climbStairs(self, n: int) -> int:
        pre, cur = 1, 1

        for i in range(2, n+1):
            pre, cur = cur, pre + cur

        return cur