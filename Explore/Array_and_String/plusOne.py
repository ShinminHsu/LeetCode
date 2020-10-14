class Solution:
    def plusOne(self, digits):

        carry = 1
        n = len(digits)

        for i in range(n-1, -1, -1):
            carry, digit_i = divmod(digits[i] + carry, 10)
            digits[i] = digit_i
            if carry == 0:
                return digits

        return [1, *digits]


digits = list(map(int, input().split()))
s = Solution()
print(s.plusOne(digits))