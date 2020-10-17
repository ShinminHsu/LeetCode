class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        minLen = len(strs[0])
        for s in strs:
            minLen = min(minLen, len(s))

        low = 0
        high = minLen

        """
        if all the strings contain from low to middle
        then check if they contain from middle+1 to (middle+high) / 2
        therefore, low should be middle+1 now
        else if they dont contain the substring, let high be middle - 1
        """
        while low <= high:
            middle = (low + high) // 2
            if self.checkPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1

        return strs[0][:((low + high) // 2)]


    def checkPrefix(self, strs, end):
        """
        Check if all the strings contain the substring from the start to the end
        """
        substring = strs[0][:end]
        for s in strs:
            if not s.startswith(substring):
                return False
        return True

strs = ["radog","racecar","racar"]
s = Solution()
print(s.longestCommonPrefix(strs))
