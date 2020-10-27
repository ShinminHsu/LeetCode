class Solution:
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

    def reverseWords2(self, s):
        return " ".join(word[::-1] for word in s.split())

s = "  Bob    Loves  Alice   "
solution = Solution()
print(solution.reverseWords2(s))
