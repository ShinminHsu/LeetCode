class Solution:
    def numSquares(self, n: int) -> int:

        queue = set()
        i = 1
        while i ** 2 <= n:
            queue.add(i ** 2)
            i += 1

        step = 0
        toCheck = [n]

        while toCheck:
            step += 1
            check_size = len(toCheck)
            for _ in range(check_size):
                num = toCheck.pop(0)
                if num in queue:
                    return step

                for x in queue:
                    if x <= num:
                        toCheck.append(num - x)

        return step

s = Solution()
print(s.numSquares(12))
