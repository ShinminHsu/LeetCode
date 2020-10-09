class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count, h = 0, []
        
        for c in s:
            if c in h:
                h = h[h.index(c)+1:]

            h.append(c)
            max_count = (max_count, len(h))
        return max(max_count, len(h))

## Copy from others
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = {}
        max_so_far = curr_max = start = 0
        for index, i in enumerate(s):
            if i in dct and dct[i] >= start:
                max_so_far = max(max_so_far, curr_max)
                curr_max = index - dct[i]
                start = dct[i] + 1
            else:
                curr_max += 1
            dct[i] = index
        return max(max_so_far, curr_max)



s = Solution1()
print(s.lengthOfLongestSubstring("aab"))