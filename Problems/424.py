import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the maximum frequency of character in each sliding window
        
        ABAABA     replace_count
        l   r     ->  2 == k
          r
        """

        counter = collections.defaultdict(lambda: 0)
        res = 0
        left = 0
        
        for right in range(len(s)):

            counter[s[right]] += 1
            replace_count = (right - left + 1) - max(counter.values())

            if replace_count == k:
                res = max(res, right - left + 1)

            elif replace_count > k:
                counter[s[left]] -= 1
                left += 1

        return res

s = 'ABAB'
k = 0
a = Solution()
print(a.characterReplacement(s, k))