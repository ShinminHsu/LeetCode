class Solution:
    def strStr(self, haystack, needle):
        """
        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        :param haystack: str
        :param needle: str
        :return: int
        """

        if not haystack and not needle:
            return 0
        if not needle:
            return -1

        n = len(haystack)
        m = len(needle)
        pi = self.computePrefix(needle)
        q = 0  # number of characters matched

        for i in range(n):
            while q > 0 and needle[q] != haystack[i]:
                q = pi[q-1]  # next character does not match
            if needle[q] == haystack[i]:
                q += 1  # next character matches
            if q == m:
                return i+1-m
                # q = pi[q-1]

        return -1

    def computePrefix(self, needle):
        m = len(needle)
        pi = [0] * m
        k = 0

        for q in range(1, m):
            while k > 0 and needle[k] != needle[q]:
                k = pi[k-1]
            if needle[k] == needle[q]:
                k += 1
            pi[q] = k

        return pi


haystack = 'ABABACABABAB'
needle = 'ABABA'
s = Solution()
s.strStr(haystack, needle)