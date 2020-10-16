class Solution:
    def strStr(self, haystack, needle):
        """
        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        :param haystack: str
        :param needle: str
        :return: int
        """

        return -1

    def computePrefix(self, haystack, needle):
        m = len(needle)
        pi = [0]
        k = 0

        for q in range(1, m):
            while k > 0 and needle[k + 1] != pi[q]:
                k = pi[k]
            if needle[k + 1] == needle[q]:
                k += 1
            pi[q] = k
