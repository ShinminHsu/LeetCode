class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1       # 2 ** 31 - 1 = 2147483647
        
        remainder = abs(x)
        reverse = 0

        while remainder:
            remainder, digit = divmod(remainder, 10)
            if reverse > INT_MAX  // 10:  # overflow
                return 0

            reverse = reverse * 10 + digit
        
        if x < 0:
            reverse = - reverse
        
        return reverse

s = Solution()
print(s.reverse(-123))