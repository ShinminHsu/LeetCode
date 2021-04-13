class Solution:
    def firstUniqChar(self, s: str) -> int:

        hash_map = {}

        # build a hash map for storing the occurances of all characters
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        # find the index
        for i, char in enumerate(s):
            if hash_map[char] == 1:
                return i

        return -1


