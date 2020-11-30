class Solution:
    def climbStairs_DP(self, n: int) -> int:

        hash_table = {0: 0, 1: 1, 2: 2}
        if n in hash_table:
            return hash_table[n]

        for i in range(3, n + 1):
            hash_table[i] = hash_table[i - 1] + hash_table[i - 2]

        return hash_table[n]

    def climbStairs(self, n: int) -> int:

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        one_step_before, two_steps_before = 2, 1

        for i in range(3, n + 1):
            all_ways = one_step_before + two_steps_before
            one_step_before, two_steps_before = all_ways, one_step_before

        return all_ways
